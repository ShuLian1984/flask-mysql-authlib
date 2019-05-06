#from .account import account as account_blueprint
from authlib.flask.oauth2 import AuthorizationServer, ResourceProtector
from authlib.flask.oauth2.sqla import (
    create_query_client_func,
    create_save_token_func,
    create_revocation_endpoint,
    create_bearer_token_validator,
)
from project.models import db, OAuth2Client, OAuth2Token

require_oauth = ResourceProtector()
query_client = create_query_client_func(db.session, OAuth2Client)
save_token = create_save_token_func(db.session, OAuth2Token)
authorization = AuthorizationServer(
    query_client=query_client,
    save_token=save_token,
)



from authlib.specs.rfc6749 import grants
from werkzeug.security import gen_salt
from .admin import admin as admin_blueprint
from .oauth2blueprint import oauth2bp as oauth2_blueprint


def init_app(app):
    #app.register_blueprint(main_blueprint)
    #app.register_blueprint(account_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(oauth2_blueprint)
