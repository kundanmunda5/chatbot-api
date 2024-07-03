from app.extensions import db

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(256))
    bot_response = db.Column(db.String(256))

    def __repr__(self):
        return f'<ChatLog {self.user_input} - {self.bot_response}>'

