#from .oauth2 import config_oauth
from authlib.specs.rfc6749 import grants
from werkzeug.security import gen_salt
from project.models import db
#from project.models.user import User
from project.models.oauth2client import OAuth2Client
from project.models.oauth2authorizationcode import OAuth2AuthorizationCode
from project.models.oauth2token import OAuth2Token
from project.models.anonymoususer import AnonymousUser

from .authorizationcodegrant import AuthorizationCodeGrant
from .passwordgrant import PasswordGrant
from .refreshtokengrant import RefreshTokenGrant

from authlib.flask.oauth2 import AuthorizationServer, ResourceProtector
from flask_login import LoginManager

from authlib.flask.oauth2.sqla import (
    create_query_client_func,
    create_save_token_func,
    create_revocation_endpoint,
    create_bearer_token_validator,
)

# Set up Flask-Login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'

query_client = create_query_client_func(db.session, OAuth2Client)
save_token = create_save_token_func(db.session, OAuth2Token)
authorization = AuthorizationServer(
    query_client=query_client,
    save_token=save_token,
)
require_oauth = ResourceProtector()


def init_app(app):
    authorization.init_app(app)

    # support all grants
    authorization.register_grant(grants.ImplicitGrant)
    authorization.register_grant(grants.ClientCredentialsGrant)
    authorization.register_grant(AuthorizationCodeGrant)
    authorization.register_grant(PasswordGrant)
    authorization.register_grant(RefreshTokenGrant)

    # support revocation
    revocation_cls = create_revocation_endpoint(db.session, OAuth2Token)
    authorization.register_endpoint(revocation_cls)

    # protect resource
    bearer_cls = create_bearer_token_validator(db.session, OAuth2Token)
    require_oauth.register_token_validator(bearer_cls())

    login_manager.anonymous_user = AnonymousUser
