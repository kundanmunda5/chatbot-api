from flask import request, jsonify
from app.main import main
from app.services.chat_services import get_chat_response, fetch_chat_response




@main.route('/test/chat', methods=['POST'])
def test_chat():
    user_input = request.json.get('message')
    response = get_chat_response(user_input)
    return jsonify(response)

@main.route('/v1/chat', methods=['POST'])
def chat():
    user_id = request.json.get('user_id')
    user_query = request.json.get('query')
    user_access_token = request.json.get('access_token')
    stock_ticker_access_key = request.json.get('stock_ticker_access_key')

    if not user_id or not user_access_token or not stock_ticker_access_key:
        response = { "error" : "INVALID REQUEST OR INVALID CREDENTIALS AND TOKENS"}
        return jsonify(response), 403

    response = fetch_chat_response(user_id = user_id,
                                       user_query = user_query,
                                       user_access_token = user_access_token,
                                       stock_ticker_access_key = stock_ticker_access_key
                                       )


    # response = get_chat_response(user_input)


    return jsonify(response), 200
