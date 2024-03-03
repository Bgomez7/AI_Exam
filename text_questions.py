import google.generativeai as genai


# input text from source to create questions
class TextQuestions:
    # constructor
    def __init__(self, text_src):
        # Gemini model and chat initialization
        self.model = genai.GenerativeModel('gemini-1.0-pro-001')
        self.text_chat = self.model.start_chat(history=[])

        # text src and question initialization
        self.text_src = text_src
        self.current_question_number = 1

    # to_string method for debugging purposes
    def __str__(self):
        return_string = ""
        # count = 0
        for message in self.text_chat.history:
            # if count % 2 != 0:
            return_string += f"\nNew\n\n{message.parts[0].text}End"
            # count += 1
        return return_string

    def generate_questions(self, num_questions, num_choices):
        response = self.text_chat.send_message(
            # Topic, number of questions and choices per question
            f"Give me {num_questions} multiple-choice questions with {num_choices} choices using the following text: "
            f"\"{self.text_src}\"."
            # 1. (no indentations preceding number)
            f" Start the question number with {self.current_question_number}. and have no indentations preceding the "
            # 1. What is a question?
            f"question number. After the question number add a space, followed by the question. "
            #   (a)
            f"Have the choice markers be preceded by an indentation once and have the format (a), "
            #   (a), (b), ... (z)
            f"where we have a lowercase letter wrapped in parentheses. The choice markers will follow alphabetical "
            f"order starting from \"a\" and ending with \"z\" if there are enough choices. "
            #   (a) choice1 \n, (b) choice2 \n, ... (z) choice26
            f"Following the letter marker, add a space and then the "
            f"choice. Keep each choice in their own line."
            f"After all questions have been listed, have a python list with answers to the questions."
            # [a, b, a, d] (Answer key)
        )
        self.current_question_number += num_questions  # keep track of the number of questions

    # generate subsequent sets of questions
    def add_question(self, num_questions, num_choices):
        response = self.text_chat.send_message(
            f"After the last set of questions add {num_questions} more multiple-choice questions with {num_choices} "
            f"choices over the same text from the first input. Start the new set of questions with the question number "
            f"{self.current_question_number}. Add the answers to the python list of answers and keep the list at the "
            f"end of the questions. Keep all other formatting the same."
        )
        self.current_question_number += num_questions  # keep track of the number of questions

    # regenerate a specific question
    def alter_question(self, question_number, num_choices):
        response = self.text_chat.send_message(
            f"Replace the {question_number}. question with a new one in its place and have the number of choices be "
            f"{num_choices}. Keep the formatting the same. Update the answer in the python list to correspond to the "
            f"new question."
        )
