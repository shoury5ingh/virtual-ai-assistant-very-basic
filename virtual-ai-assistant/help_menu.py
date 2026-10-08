"""help_menu.py - Help text (FR-10)."""

COMMANDS = [
    ("time", "show current time"),
    ("date", "show current date"),
    ("calculate", "do a calculation, e.g. calculate 12 + 8"),
    ("joke", "tell a joke"),
    ("quote", "motivational quote"),
    ("fact", "random fact"),
    ("game", "play number guessing game"),
    ("recommend", "activity suggestion (rule-based AI demo)"),
    ("perceptron", "artificial neuron demo (deep learning concept)"),
    ("help", "show this menu"),
    ("exit", "quit the assistant"),
]


def print_help():
    print("Assistant:")
    for command, description in COMMANDS:
        print(f"  - {command:<12}{description}")