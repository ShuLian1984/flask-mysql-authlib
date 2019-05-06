import time
#from project.api.models import User
#from flask_sqlalchemy import SQLAlchemy
from project.shared.database import db

from authlib.flask.oauth2.sqla import (
    OAuth2ClientMixin,
    OAuth2AuthorizationCodeMixin,
    OAuth2TokenMixin,
)


class OAuth2Client(db.Model, OAuth2ClientMixin):
    __tablename__ = 'oauth2_client'
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}

    print("Table is _", __tablename__)
    #parent = db.relationship('User', backref=backref('OAuth2Client', passive_deletes=True))
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))

    user = db.relationship('User')
    #user = db.relationship('User', backref=backref('OAuth2Client', passive_deletes=True))
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
    #    nullable=False)
    #user = db.relationship('User',
    #    backref=db.backref('users', lazy=True))


class OAuth2AuthorizationCode(db.Model, OAuth2AuthorizationCodeMixin):
    __tablename__ = 'oauth2_code'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User')


class OAuth2Token(db.Model, OAuth2TokenMixin):
    __tablename__ = 'oauth2_token'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User')

    def is_refresh_token_expired(self):
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at < time.time()
