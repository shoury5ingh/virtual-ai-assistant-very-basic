# virtual-ai-assistant-very-basic
Rule-based virtual assistant (Mini Alexa) in pure Python with a console app and a Tkinter GUI. Offline, standard library only. Demonstrates rule-based AI, intent recognition and a simple perceptron (neural network) demo.

# Virtual AI Assistant (Mini Alexa)

A text-based, rule-based virtual assistant built in Python for the Nexbridge Technologies
AI Internship Program (Project 1). It runs completely offline using only the Python
standard library, with no external APIs, datasets or ML libraries.

It comes in two versions: a **console app** (`main.py`) and an optional **Tkinter chat window** (`gui.py`).

## Features
- Greets you, asks your name and remembers it for the session
- Shows the current date and time
- Calculator (+, -, *, /) with divide-by-zero and invalid-input handling
- Random motivational quotes, jokes and facts
- Number guessing game (1-20, 5 tries, higher/lower hints)
- Rule-based activity recommendation based on the time of day
- Perceptron demo: inputs, weights, bias, step activation and a small second layer
- Help menu, friendly fallback for unknown input, graceful exit

## How to run
Requires Python 3.8+. No installation needed.

    python main.py      # console version
    python gui.py       # Tkinter GUI version

On some Linux systems, install Tkinter first: `sudo apt install python3-tk`

## Example commands
    time
    calculate 12 + 8
    joke
    game
    recommend
    perceptron
    help
    exit

## Project structure
    virtual-ai-assistant/
    |-- main.py            # console entry point, main loop and intent detection
    |-- gui.py             # optional Tkinter chat window
    |-- greetings.py       # name capture and greeting
    |-- datetime_utils.py  # date and time
    |-- calculator.py      # expression parsing and arithmetic
    |-- content.py         # quotes, jokes, facts
    |-- game.py            # number guessing game
    |-- ai_concepts.py     # rule-based recommendation and perceptron demo
    |-- help_menu.py       # help text
    |-- test_inputs.txt    # sample inputs for quick testing
    |-- README.md

## AI / ML / DL concepts demonstrated
| Concept | Where in the code |
| --- | --- |
| Rule-based system, keyword detection, intent recognition | `detect_intent()` in `main.py` |
| Decision tree / classification analogy | `recommend_activity()` in `ai_concepts.py` |
| Recommendation logic | random selection in `content.py` |
| Neuron, weights, bias, activation, forward propagation, hidden layer | `neuron()` and `perceptron_demo()` in `ai_concepts.py` |
| Session memory | user name stored and reused in replies |

No models are trained. The ML/DL ideas are shown with plain Python arithmetic.

## Testing
    python main.py < test_inputs.txt

## Future improvements
- Save conversation history to a file
- Train a real classifier with scikit-learn
- Voice input/output
- Real neural networks with TensorFlow or PyTorch

python, ai, virtual-assistant, chatbot, tkinter, rule-based, perceptron, machine-learning, deep-learning, beginner-project, internship
