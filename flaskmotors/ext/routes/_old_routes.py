from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint

from flaskmotors.ext.models.welcomemod import WelcomeModel
from flaskmotors.ext.schemas.welcomesc import WelcomeSchema

rt_api = Blueprint('api', __name__)


@rt_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeSchema
        }
    }
})
def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = WelcomeModel()
    return WelcomeSchema().dump(result), 200
