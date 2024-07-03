from flask import Flask, request, jsonify
import time
import logging
import threading
import chatbot


app = Flask(__name__)


#Set up logging
def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        #format='%(asctime)s - %(name)s - %(levelname)s - [Thread %(thread)d] - %(message)s',
        format='%(asctime)s - %(levelname)s - [Thread %(thread)d] - %(message)s'
    )
    # Remove all handlers associated with the root logger object
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Add your own handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [Thread %(thread)d] - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [Thread %(thread)d] - %(message)s')
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)


setup_logging()

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s -  [Thread %(thread)d] - %(message)s')

logger = logging.getLogger(__name__)


#---------------API ENDPOINTS--------------------

@app.route("/") #healthcheck
def health_check():
    message,status = chatbot.healthcheck()
    response = {"message":message,
            "status" : status}
    return jsonify(response),200
     

@app.route("/chat")
def check_connection():
    message = f"Connection successful. For more details refer the documentation..."
    status = "success"
    response = {"message" : message,
                 "status": status}
    return jsonify(response), 200

@app.route("/chat", methods = ["POST"])
def start_conversation():

    token_id = ""
    user_id = ""
    conversation_meta = ""
    message , status = chatbot.start_conversation()
    session_id = ""
    token_id = ""
    user_id = ""
    conversation_meta = ""

    return jsonify({"message": message, "status": status}), 200
    


if __name__ == "__main__":
    app.run(debug=True, port=5050)