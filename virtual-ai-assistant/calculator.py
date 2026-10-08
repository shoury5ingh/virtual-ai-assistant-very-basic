"""
calculator.py : Basic arithmetic (FR-05).

Parses text like "calculate 12 + 8" or "12 * 3" into two numbers and an
operator. Invalid input never crashes the program (try/except).
"""

OPERATORS = ("+", "-", "*", "/")


def parse_expression(text):
    """
    Extract (num1, operator, num2) from text.

    Returns None if no valid expression is found. Raises ValueError if the
    numbers cannot be converted.
    """
    # Allow 'x' as a friendly alias for multiplication.
    cleaned = text.replace("calculate", "").replace(" x ", " * ").strip()

    # Search for an operator, skipping position 0 so negative numbers work.
    for index, char in enumerate(cleaned):
        if index > 0 and char in OPERATORS:
            left = cleaned[:index].strip()
            right = cleaned[index + 1:].strip()
            if left and right:
                return float(left), char, float(right)
    return None


def calculate(num1, operator, num2):
    """Apply the operator to the two numbers and return the result."""
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2  # ZeroDivisionError handled by the caller
    raise ValueError("Unknown operator")


def format_number(value):
    """Show 20.0 as 20 but keep 2.5 as 2.5."""
    return str(int(value)) if value == int(value) else str(round(value, 4))


def run_calculator(text):
    """Full calculator flow: parse, compute, return a friendly message."""
    try:
        parsed = parse_expression(text)
        if parsed is None:
            return "Try something like: calculate 12 + 8"
        num1, operator, num2 = parsed
        return f"The result is {format_number(calculate(num1, operator, num2))}"
    except ZeroDivisionError:
        return "I can't divide by zero - try a different number."
    except ValueError:
        return "Those don't look like valid numbers. Try: calculate 12 + 8"