"""datetime_utils.py - Date and time reporting (FR-03, FR-04)."""

from datetime import datetime


def get_current_time():
    """Return the current time, e.g. 'It's currently 3:45 PM.'"""
    now = datetime.now()
    # %I gives a zero-padded hour, so strip the leading zero for readability.
    return "It's currently " + now.strftime("%I:%M %p").lstrip("0") + "."


def get_current_date():
    """Return today's date, e.g. 'Today is Thursday, 08 October 2026.'"""
    return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
