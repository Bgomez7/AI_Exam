import google.generativeai as genai


class TopicQuestions:
    def __init__(self, topic):
        # Gemini and chat initialization
        self.model = genai.GenerativeModel('gemini-1.0-pro-001')
        self.topic_chat = self.model.start_chat(history=[])

        # topic and current question initialization
        self.topic = topic
        self.current_question_number = 1

