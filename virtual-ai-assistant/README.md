# Virtual AI Assistant (Mini Alexa)

Nexbridge Technologies - AI Internship Program, Project 1 (AI-INT-P1-VAA).
A text based, rule based assistant that runs offline using only the Python standard library.

## Run
```
python main.py
```
Requires Python 3.8+. No installs, no internet.

## Commands
| Command | What it does |
| --- | --- |
| time / date | Current time / date |
| calculate 12 + 8 | Arithmetic (+, -, *, /) with error handling |
| joke / quote / fact | Random item from a predefined list |
| game | Number guessing game (1-20, 5 tries) |
| recommend | Rule-based activity suggestion by hour (AI/ML demo) |
| perceptron | Single artificial neuron + tiny second layer (DL demo) |
| help | List commands |
| exit / quit / bye | Quit |

## Structure
`main.py` (loop + intent detection), `greetings.py`, `datetime_utils.py`, `calculator.py`,
`content.py`, `game.py`, `ai_concepts.py`, `help_menu.py`.

## How AI / ML / DL concepts map to the code
- **Rule-based system / intent recognition / keyword detection** - `detect_intent()` in `main.py`.
- **Decision tree / classification analogy** - `recommend_activity()` in `ai_concepts.py` (hour = feature, activity = class).
- **Recommendation logic** - random selection in `content.py`.
- **Neuron, weights, bias, activation, forward propagation, hidden layer** - `neuron()` and `perceptron_demo()` in `ai_concepts.py` (nothing is trained).
- **Session memory** - user name stored in `main()` and reused in replies.

## Testing
Manual checklist from the PRD Section 33 was run; see `test_inputs.txt` for sample input.
Quick run: `python main.py < test_inputs.txt`