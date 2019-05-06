from .base import db
from .user import User
from .role import Role
from .editablehtml import EditableHTML

from authlib.flask.oauth2.sqla import (
    OAuth2ClientMixin,
    OAuth2AuthorizationCodeMixin,
    OAuth2TokenMixin,
)
from .oauth2authorizationcode import OAuth2AuthorizationCode
from .oauth2client import OAuth2Client
from .oauth2token import OAuth2Token
from .user import User
#from .post import Post
from .role import Role
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash
from .permission import Permission


def init_app(app):
    db.init_app(app)
