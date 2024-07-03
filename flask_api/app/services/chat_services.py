#Import the ChatBot App Package and get the response
class ChatBot:
    def __init__(self):
        self.responses = {
            "user": "Hi there! How can I help you today?",
            "how are you": "I'm good, thank you! How about you?",
            "bye": "Goodbye! Have a great day!",
            "default": "Sorry, I didn't understand that."
        }
    
    def fetch_chat_response(self, user_id, user_query, user_access_token, stock_ticker_access_key):
        response = {
            'user_id' : user_id,
            'query_received': user_query,
            'bot_response' : {
                'message' : "This is the chat message from the ChatBot!",
                'recommendation': "This would be a json_dump_response of the recommendation_data",
                'follow_up_query': ["This would be a list of generated follow_up queries"],
                }
        }
        return response


def get_chat_response(user_input) -> dict:
    # Mock response, replace with actual chatbot logic
    return {"response": f"You said: {user_input}"}



def fetch_chat_response(user_id, user_query, user_access_token, stock_ticker_access_key) -> dict:
    chatbot = ChatBot()
    return chatbot.fetch_chat_response(user_id = user_id,
                                       user_query = user_query,
                                       user_access_token = user_access_token,
                                       stock_ticker_access_key = stock_ticker_access_key
                                       )
