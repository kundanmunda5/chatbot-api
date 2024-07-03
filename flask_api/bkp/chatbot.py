import importlib.util
import sys

# Specify the path to the script
script_path = '/home/ubuntu/LatestSageMaker/Chatbot/version_1/Untitled Folder/main_chat_body_with_redis_connection.py'

# Load the module
spec = importlib.util.spec_from_file_location("main_chat_body_with_redis_connection", script_path)
chatbot = importlib.util.module_from_spec(spec)
sys.modules["main_chat_body_with_redis_connection"] = chatbot
spec.loader.exec_module(chatbot)

# Now you can use the functions and classes from the script
# For example, if there is a function named `my_function` in the script, you can call it like this:
# module.my_function()

def start_conversation():
    chatbot.main()

    