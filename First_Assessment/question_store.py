import json
import os

FILE_NAME = "questions.json"

# Load all quiz questions from JSON file
def load_questions():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save updated question collection to JSON file
def save_questions(questions):
    with open(FILE_NAME, "w") as file:
        json.dump(questions, file, indent=4)
