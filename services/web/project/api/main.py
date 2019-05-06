import os
import logging
from authlib.flask.oauth2 import current_token
from authlib.specs.rfc6749 import OAuth2Error
from flask import Blueprint, jsonify, request, render_template, redirect


LOGGER = logging.getLogger('gunicorn.error')

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    LOGGER.info('Hitting the "/ping" route')
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


@main_blueprint.route('/secret', methods=['POST'])
def secret():
    LOGGER.info('Hitting the "/secret" route')
    response_object = {
        'status': 'success',
        'message': 'nay!',
        'container_id': os.uname()[1]
    }
    #SECRET_CODE = open('/run/secrets/secret_code', 'r').read().strip()

    #if request.get_json().get('secret') == SECRET_CODE:
    #    response_object['message'] = 'yay!'
    return jsonify(response_object)
