"""
gui.py - Optional Tkinter chat window for Mini Alexa.

Run with:  python gui.py

The assistant's logic lives in the Assistant class (no Tkinter inside), so it
reuses the same modules as the console version: intent detection from main.py,
calculator.py, content.py, datetime_utils.py, ai_concepts.py, game.py settings.

Because a window can't block on input(), multi-step features (name capture,
guessing game, perceptron) are handled with a small state machine: the
`state` attribute remembers what the assistant is waiting for.
"""

import random
import tkinter as tk
from tkinter import scrolledtext

import ai_concepts
import calculator
import content
import datetime_utils
import game
import greetings
import help_menu
from main import detect_intent, normalize

PERCEPTRON_PROMPTS = ["Free time (0-1)", "Good weather (0-1)", "Energy level (0-1)"]


class Assistant:
    """Chat logic: respond(text) returns a list of reply lines."""

    def __init__(self):
        self.user_name = None
        self.state = "ask_name"   # ask_name | idle | calc | game | perceptron
        self.finished = False
        # guessing-game session data
        self.secret = 0
        self.attempts = 0
        # perceptron session data
        self.inputs = []

    def start(self):
        return [f"Hi! I'm {greetings.ASSISTANT_NAME}. What's your name?"]

    def respond(self, text):
        text = text.strip()
        if self.state == "ask_name":
            return self._set_name(text)
        if self.state == "game":
            return self._game_guess(text)
        if self.state == "perceptron":
            return self._perceptron_input(text)
        if self.state == "calc":
            self.state = "idle"
            return [calculator.run_calculator(normalize(text))]
        return self._handle_command(text)

    # ----- state handlers -------------------------------------------------
    def _set_name(self, text):
        self.user_name = text.title() if text else "Friend"
        self.state = "idle"
        return [greetings.build_greeting(self.user_name)]

    def _handle_command(self, text):
        cleaned = normalize(text)
        intent = detect_intent(cleaned)

        if intent == "exit":
            self.finished = True
            return [f"Goodbye, {self.user_name}! Have a great day."]
        if intent == "greeting":
            return [f"Hello again, {self.user_name}!"]
        if intent == "time":
            return [datetime_utils.get_current_time()]
        if intent == "date":
            return [datetime_utils.get_current_date()]
        if intent == "calculate":
            if cleaned == "calculate":
                self.state = "calc"
                return ["What should I calculate? (e.g. 12 + 8)"]
            return [calculator.run_calculator(cleaned)]
        if intent == "quote":
            return [content.get_random_quote()]
        if intent == "joke":
            return [content.get_random_joke()]
        if intent == "fact":
            return [content.get_random_fact()]
        if intent == "recommend":
            return [f"{self.user_name}, {ai_concepts.recommend_activity()}"]
        if intent == "help":
            return ["Here's what I can do:"] + [
                f"  - {c:<12}{d}" for c, d in help_menu.COMMANDS]
        if intent == "game":
            return self._start_game()
        if intent == "perceptron":
            return self._start_perceptron()
        return ["I'm not sure I understood that - type 'help' to see what I can do."]

    # ----- guessing game --------------------------------------------------
    def _start_game(self):
        self.secret = random.randint(game.LOW, game.HIGH)
        self.attempts = 0
        self.state = "game"
        return [f"I'm thinking of a number between {game.LOW} and {game.HIGH}. "
                f"You have {game.MAX_ATTEMPTS} tries. Guess a number:"]

    def _game_guess(self, text):
        self.attempts += 1
        try:
            guess = int(text)
        except ValueError:
            guess = None  # invalid guess still uses up the attempt

        if guess == self.secret:
            self.state = "idle"
            return [f"Correct! You got it in {self.attempts} "
                    f"{'try' if self.attempts == 1 else 'tries'}!"]

        if guess is None:
            hint = "That's not a whole number!"
        else:
            hint = "Higher!" if guess < self.secret else "Lower!"

        if self.attempts >= game.MAX_ATTEMPTS:
            self.state = "idle"
            return [hint, f"Out of tries! The number was {self.secret}. "
                          "Better luck next time."]
        return [f"{hint} ({game.MAX_ATTEMPTS - self.attempts} tries left)"]

    # ----- perceptron demo ------------------------------------------------
    def _start_perceptron(self):
        self.inputs = []
        self.state = "perceptron"
        return ["Perceptron demo - history's simplest neural network unit.",
                f"Fixed weights = {ai_concepts.WEIGHTS}, bias = {ai_concepts.BIAS}",
                "Think: how interested are you in going out today?",
                f"Enter {PERCEPTRON_PROMPTS[0]}:"]

    def _perceptron_input(self, text):
        try:
            self.inputs.append(float(text))
        except ValueError:
            self.state = "idle"
            return ["Please enter numbers like 0.7 - type 'perceptron' to try again."]

        if len(self.inputs) < len(PERCEPTRON_PROMPTS):
            return [f"Enter {PERCEPTRON_PROMPTS[len(self.inputs)]}:"]

        self.state = "idle"
        total, output = ai_concepts.neuron(self.inputs)
        terms = " + ".join(f"({x}*{w})" for x, w in zip(self.inputs, ai_concepts.WEIGHTS))
        _, final = ai_concepts.neuron([output], weights=[1.0], bias=-0.5)
        verdict = "Yes, go out!" if final == 1 else "Maybe stay in today."
        return [f"Weighted sum + bias = {terms} + ({ai_concepts.BIAS}) = {round(total, 3)}",
                f"Step activation -> output = {output}",
                f"Second layer (takes output {output} as input) -> {final}",
                f"Forward propagation complete. Decision: {verdict}"]


class ChatWindow:
    """Tkinter front end: chat log, text entry, send button, quick buttons."""

    BG, PANEL = "#f4f6fb", "#ffffff"
    USER_COLOR, BOT_COLOR = "#1a56db", "#0e7c5a"

    def __init__(self, root):
        self.root = root
        self.assistant = Assistant()
        root.title("Mini Alexa - Virtual Assistant")
        root.geometry("560x640")
        root.minsize(420, 480)
        root.configure(bg=self.BG)

        tk.Label(root, text="MINI ALEXA", font=("Helvetica", 16, "bold"),
                 bg="#1f2937", fg="white", pady=10).pack(fill="x")

        self.log = scrolledtext.ScrolledText(
            root, wrap="word", state="disabled", font=("Consolas", 11),
            bg=self.PANEL, relief="flat", padx=10, pady=10)
        self.log.pack(fill="both", expand=True, padx=10, pady=(10, 5))
        self.log.tag_config("user", foreground=self.USER_COLOR, font=("Consolas", 11, "bold"))
        self.log.tag_config("bot", foreground=self.BOT_COLOR)

        # Quick-command buttons (they just send the command text)
        quick = tk.Frame(root, bg=self.BG)
        quick.pack(fill="x", padx=10)
        for cmd in ["time", "date", "joke", "quote", "fact", "game",
                    "recommend", "perceptron", "help"]:
            tk.Button(quick, text=cmd, command=lambda c=cmd: self.send(c),
                      relief="groove", padx=4).pack(side="left", padx=2, pady=4)

        entry_row = tk.Frame(root, bg=self.BG)
        entry_row.pack(fill="x", padx=10, pady=(2, 10))
        self.entry = tk.Entry(entry_row, font=("Consolas", 12))
        self.entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.entry.bind("<Return>", lambda _e: self.send())
        tk.Button(entry_row, text="Send", command=self.send, bg="#1a56db",
                  fg="white", padx=14).pack(side="left", padx=(6, 0))
        self.entry.focus_set()

        for line in self.assistant.start():
            self.add("Assistant", line, "bot")

    def add(self, who, text, tag):
        self.log.config(state="normal")
        self.log.insert("end", f"{who}: ", tag)
        self.log.insert("end", text + "\n\n" if tag == "user" else text + "\n",
                        "bot" if tag == "bot" else None)
        self.log.config(state="disabled")
        self.log.see("end")

    def send(self, text=None):
        if self.assistant.finished:
            return
        if text is None:
            text = self.entry.get()
            self.entry.delete(0, "end")
        if not text.strip() and self.assistant.state != "ask_name":
            return
        self.add("You", text, "user")
        for line in self.assistant.respond(text):
            self.add("Assistant", line, "bot")
        self.log.config(state="normal"); self.log.insert("end", "\n"); self.log.config(state="disabled")
        if self.assistant.finished:
            self.root.after(1500, self.root.destroy)  # close after goodbye


def main():
    root = tk.Tk()
    ChatWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()