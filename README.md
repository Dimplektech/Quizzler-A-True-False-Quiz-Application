# Quizzler: A True/False Quiz Application

This project is a simple quiz game built using Python and the Tkinter library for the graphical user interface (GUI). The questions are fetched from the Open Trivia Database API, and the game lets users answer True/False questions, while keeping track of their score.

## Features

- Fetches random questions using the Open Trivia Database API.
- User-friendly GUI built using Tkinter.
- Displays the current score as the user answers questions.
- Changes the background color based on whether the user's answer was correct or incorrect.
- Automatically displays the final score when all questions have been answered.

## Project Structure

- `main.py`: This file initializes the game and starts the quiz application.
- `question_model.py`: Contains the `Question` class, representing a quiz question.
- `data.py`: Fetches quiz questions from the Open Trivia Database API.
- `quiz_brain.py`: Manages the quiz logic, including checking answers and keeping track of the current question.
- `ui.py`: Manages the graphical interface, displaying questions and handling user input.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with standard Python installations)
- Internet connection (to fetch questions from the Open Trivia Database API)

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/quiz-app.git
