"""
greetings.py - Greeting logic and name capture (FR-01, FR-02).

AI concept: Human-Computer Interaction. Every conversational assistant
starts by opening a dialogue and storing a little session state.
"""

ASSISTANT_NAME = "Mini Alexa"


def get_user_name():
    """Ask for the user's name; fall back to 'friend' if left blank."""
    print(f"Assistant: Hi! I'm {ASSISTANT_NAME}. What's your name?")
    name = input("You: ").strip()
    return name.title() if name else "Friend"


def build_greeting(user_name):
    """Return the welcome message shown right after the name is captured."""
    return (f"Nice to meet you, {user_name}! "
            "Type 'help' to see what I can do.")