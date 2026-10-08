"""game.py - Number guessing game (FR-09)."""

import random

LOW, HIGH = 1, 20
MAX_ATTEMPTS = 5


def play_guessing_game():
    """Run one round: limited attempts, with higher/lower hints."""
    secret = random.randint(LOW, HIGH)
    print(f"Assistant: I'm thinking of a number between {LOW} and {HIGH}. "
          f"You have {MAX_ATTEMPTS} tries.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        raw = input(f"Guess #{attempt}: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            # An invalid guess still uses up the attempt (keeps the limit strict).
            print("Assistant: That's not a whole number!")
            continue

        if guess == secret:
            print(f"Assistant: Correct! You got it in {attempt} "
                  f"{'try' if attempt == 1 else 'tries'}!")
            return
        print("Assistant: Higher!" if guess < secret else "Assistant: Lower!")

    print(f"Assistant: Out of tries! The number was {secret}. Better luck next time.")