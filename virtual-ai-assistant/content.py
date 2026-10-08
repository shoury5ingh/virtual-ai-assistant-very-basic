"""
content.py - Quotes, jokes and facts (FR-06, FR-07, FR-08).

AI concept: a simple "recommendation" - the assistant picks content from a
list. Here the rule is random choice; real recommenders use learned scores.
"""

import random

QUOTES = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The expert in anything was once a beginner. - Helen Hayes",
    "Success is the sum of small efforts repeated day in and day out. - R. Collier",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 types of people: those who understand binary and those who don't.",
    "Why was the Python programmer a great cook? They knew all the recipes (functions).",
    "A SQL query walks into a bar, sees two tables and asks: 'Can I join you?'",
    "Why did the neural network go to school? To improve its weights and biases.",
]

FACTS = [
    "The term 'Artificial Intelligence' was coined in 1956 at Dartmouth College.",
    "Python is named after Monty Python, not the snake.",
    "The first computer bug was a real moth found in a Harvard Mark II in 1947.",
    "The perceptron, an early neural network unit, was introduced in 1958.",
    "Honey never spoils - edible honey has been found in ancient Egyptian tombs.",
    "A day on Venus is longer than a year on Venus.",
]


def get_random_quote():
    return random.choice(QUOTES)


def get_random_joke():
    return random.choice(JOKES)


def get_random_fact():
    return random.choice(FACTS)