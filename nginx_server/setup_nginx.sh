sudo apt-get update
sudo apt-get install nginx -y


nginx_config_file="server { \n
    listen 80; \n
    server_name your_domain_or_ip; \n

    location / { \n
        proxy_pass http://127.0.0.1:5000; \n
        proxy_set_header Host $host; \n
        proxy_set_header X-Real-IP $remote_addr; \n
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; \n
        proxy_set_header X-Forwarded-Proto $scheme; \n
    } \n
}
"

echo $nginx_config_file > '/etc/nginx/sites-available/chatbot_api'

#Enabling the nginx configuration

sudo ln -s /etc/nginx/sites-available/chatbot_api /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx


