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

