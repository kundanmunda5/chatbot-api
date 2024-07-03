sudo cp /home/ubuntu/ChatBotAPI/flask_api/setup_scripts/chatbot_api.service /etc/systemd/system/

sudo systemctl start chatbot_api
sudo systemctl enable chatbot_api

