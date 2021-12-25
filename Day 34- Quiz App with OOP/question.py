import requests
import random
import html


class Question:
    # Get data from api
    def __init__(self, url):
        self.response = requests.get(url=url)
        self.response.raise_for_status()
        self.data = self.response.json()

    # Randomly chose question from data, return question and it's correct answer
    def chose_question(self):
        chosen_question = random.choice(self.data["results"])
        question = html.unescape(chosen_question["question"])
        correct_answer = chosen_question["correct_answer"]

        return question, correct_answer
