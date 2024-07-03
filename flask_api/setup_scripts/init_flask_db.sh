#Responsible to initialise the DB

flask db init
flask db migrate -m "Initial migration."
flask db upgrade

