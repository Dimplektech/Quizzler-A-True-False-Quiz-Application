"""
This module is responsible for fetching quiz questions from the Open Trivia Database API.

Functions
---------
fetch_questions(amount=10, type='boolean', category=18):
    Fetches a specified number of True/False quiz questions from the Open Trivia Database API.

Attributes
----------
question_data : list
    A list of dictionaries, each containing a question and its correct answer.
"""

import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

