from flask_rq import RQ


def init_app(app):
    RQ(app)
