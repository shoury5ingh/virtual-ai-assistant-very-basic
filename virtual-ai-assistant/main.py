"""
main.py - Entry point for Mini Alexa, a rule-based virtual assistant.

Loop: input -> normalize -> keyword match (intent) -> call module -> print.
AI concepts shown here: rule-based system, keyword detection, intent
recognition and pattern matching (the 'in' operator on lowercase text).
"""

import calculator
import content
import datetime_utils
import game
import greetings
import ai_concepts
import help_menu

EXIT_WORDS = ("exit", "quit", "bye")


def normalize(text):
    """Lowercase and strip so '  TIME ' matches 'time'."""
    return text.lower().strip()


def has_word(words, keywords):
    """Keyword detection: does any keyword appear as a whole word?"""
    return any(k in words for k in keywords)


def detect_intent(text):
    """Map normalized text to an intent name (intent recognition).

    Order matters: the first matching rule wins, like an if/elif decision tree.
    """
    words = text.split()
    if has_word(words, EXIT_WORDS):
        return "exit"
    if has_word(words, ["help", "commands", "menu"]):
        return "help"
    if has_word(words, ["perceptron", "neuron"]):
        return "perceptron"
    if has_word(words, ["recommend", "suggest", "activity"]):
        return "recommend"
    if "calculate" in words or any(op in text for op in ("+", "*", "/")) \
            or (" - " in text and any(c.isdigit() for c in text)):
        return "calculate"
    if has_word(words, ["time"]):
        return "time"
    if has_word(words, ["date", "day", "today"]):
        return "date"
    if has_word(words, ["joke", "funny"]):
        return "joke"
    if has_word(words, ["quote", "motivate", "motivation", "inspire"]):
        return "quote"
    if has_word(words, ["fact"]):
        return "fact"
    if has_word(words, ["game", "play", "guess"]):
        return "game"
    if has_word(words, ["hello", "hi", "hey"]):
        return "greeting"
    return None


def main():
    print("=" * 43)
    print("       MINI ALEXA - VIRTUAL ASSISTANT")
    print("=" * 43)
    user_name = greetings.get_user_name()
    print("Assistant:", greetings.build_greeting(user_name))

    while True:
        try:
            raw = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print()
            raw = "exit"  # Ctrl+C / Ctrl+D also exit gracefully
        intent = detect_intent(normalize(raw))

        if intent == "exit":
            break
        elif intent == "greeting":
            print(f"Assistant: Hello again, {user_name}!")
        elif intent == "time":
            print(f"Assistant: {datetime_utils.get_current_time()}")
        elif intent == "date":
            print(f"Assistant: {datetime_utils.get_current_date()}")
        elif intent == "calculate":
            if normalize(raw) == "calculate":
                raw = "calculate " + input("Assistant: What should I calculate? ")
            print(f"Assistant: {calculator.run_calculator(normalize(raw))}")
        elif intent == "quote":
            print(f"Assistant: {content.get_random_quote()}")
        elif intent == "joke":
            print(f"Assistant: {content.get_random_joke()}")
        elif intent == "fact":
            print(f"Assistant: {content.get_random_fact()}")
        elif intent == "game":
            game.play_guessing_game()
        elif intent == "recommend":
            print(f"Assistant: {user_name}, {ai_concepts.recommend_activity()}")
        elif intent == "perceptron":
            print(ai_concepts.perceptron_demo())
        elif intent == "help":
            help_menu.print_help()
        else:
            print("Assistant: I'm not sure I understood that - "
                  "type 'help' to see what I can do.")

    print(f"Assistant: Goodbye, {user_name}! Have a great day.")
    print("=" * 43)


if __name__ == "__main__":
    main()