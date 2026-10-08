"""
ai_concepts.py : Conceptual AI / ML / DL demonstrations (FR-13, FR-14).

No models are trained and no libraries are used - only plain Python.
"""

from datetime import datetime

# Rule-based decision demo (AI concept: rule based system / decision tree)

def recommend_activity(hour=None):
    """
    Recommend an activity from the hour of day using if/elif/else.
    ML analogy: the hour is the input *feature*; the activity is the
    predicted *class*. The if/elif chain is a hand-written decision tree -
    a trained classifier would learn these thresholds from data instead.
    """
    if hour is None:
        hour = datetime.now().hour

    if 5 <= hour < 9:
        return "Good morning! Time for breakfast and some stretching."
    if 9 <= hour < 12:
        return "Prime focus time - tackle your hardest task now."
    if 12 <= hour < 14:
        return "It's lunchtime - take a proper break and eat something."
    if 14 <= hour < 17:
        return "Afternoon slump? Go for a short walk or a quick coding practice."
    if 17 <= hour < 21:
        return "Evening - good time for exercise, hobbies or family time."
    return "It's late - time to rest. Good sleep helps you learn better."

# Perceptron demo (DL concept: artificial neuron / forward propagation)

WEIGHTS = [0.5, 0.3, 0.2]  # fixed multipliers, one per input (not learned!)
BIAS = -0.4                # fixed constant added to the weighted sum


def step_activation(value):
    """Step activation function: output 1 if value > 0, else 0."""
    return 1 if value > 0 else 0


def neuron(inputs, weights=WEIGHTS, bias=BIAS):
    """
    One artificial neuron: weighted sum + bias -> activation -> output.

    Returns (weighted_sum_with_bias, output).
    """
    total = sum(x * w for x, w in zip(inputs, weights)) + bias
    return total, step_activation(total)


def perceptron_demo():
    """
    Interactive perceptron: 3 inputs -> weights/bias -> step -> 0 or 1.

    Also shows a tiny 'hidden layer': a second neuron that takes the first
    neuron's output as its input, illustrating layering.
    """
    print("Assistant: Perceptron demo - history's simplest neural network unit.")
    print(f"           Fixed weights = {WEIGHTS}, bias = {BIAS}")
    print("           (Think: how interested are you in going out today?)")
    labels = ["Free time (0-1)", "Good weather (0-1)", "Energy level (0-1)"]
    inputs = []
    try:
        for label in labels:
            inputs.append(float(input(f"  {label}: ").strip()))
    except ValueError:
        return "Assistant: Please enter numbers like 0.7 - let's try again later."

    total, output = neuron(inputs)
    terms = " + ".join(f"({x}*{w})" for x, w in zip(inputs, WEIGHTS))
    print(f"  Weighted sum + bias = {terms} + ({BIAS}) = {round(total, 3)}")
    print(f"  Step activation -> output = {output}")

    # Hidden-layer illustration: neuron 2 uses neuron 1's output as its input.
    _, final = neuron([output], weights=[1.0], bias=-0.5)
    verdict = "Yes, go out!" if final == 1 else "Maybe stay in today."
    print(f"  Second layer (takes output {output} as input) -> {final}")
    return f"Assistant: Forward propagation complete. Decision: {verdict}"