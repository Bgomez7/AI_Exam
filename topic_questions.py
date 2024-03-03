import google.generativeai as genai


class TopicQuestions:
    # constructor
    def __init__(self, topic):
        # Gemini and chat initialization
        self.model = genai.GenerativeModel('gemini-1.0-pro-001')
        self.topic_chat = self.model.start_chat(history=[])

        # topic and current question initialization
        self.topic = topic
        self.current_question_number = 1

    # to_string method for debugging purposes
    def __str__(self):
        return_string = ""
        # count = 0
        for message in self.topic_chat.history:
            # if count % 2 != 0:
            return_string += f"\nNew\n\n{message.parts[0].text}End"
            # count += 1
        return return_string
