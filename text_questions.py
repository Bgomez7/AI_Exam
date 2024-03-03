import google.generativeai as genai


# input text from source to create questions
class TextQuestions:
    def __init__(self, text_src):
        # Gemini model and chat initialization
        self.model = genai.GenerativeModel('gemini-1.0-pro-001')
        self.mpc_text_chat = self.model.start_chat(history=[])

        # text src and question initialization
        self.text_src = text_src
        self.current_question_number = 1



