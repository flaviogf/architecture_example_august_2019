from flask_sqlalchemy import SQLAlchemy


class Mail:
    def init_app(self, app):
        pass

    def send(self, from_, to, subject, content):
        pass


class Sms:
    def init_app(self, app):
        pass

    def send(self, from_, to, content):
        pass


db = SQLAlchemy()
mail = Mail()
sms = Sms()
