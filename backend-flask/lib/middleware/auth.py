import os
from werkzeug.wrappers import Request, Response, ResponseStream

from lib.cognito_jwt_token import CognitoJwtToken, extract_access_token, TokenVerifyError


class auth_middleware():
    '''
    Simple WSGI middleware for Auth
    '''

    def __init__(self, app, logger):
        self.app = app
        self.logger = logger 
        self.cognito_jwt_token = CognitoJwtToken(
        user_pool_id=os.getenv("AWS_COGNITO_USER_POOL_ID"), 
        user_pool_client_id=os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
        region=os.getenv("AWS_DEFAULT_REGION"), 
        logger=logger
        )

    def __call__(self, environ, start_response):
        """
        Check validity of request, and save authed or not to request's environ. 
        """
        try:
            request = Request(environ)
            # self.logger.debug(f"{request=}")
            access_token = extract_access_token(request.headers)
            # self.logger.debug(f"{access_token=}")
            claims = self.cognito_jwt_token.verify(access_token)
            self.logger.debug("Authenicated in middleware")
            # self.logger.debug(f"{claims}")
            environ['is_authenticated'] = True
            return self.app(environ, start_response)
        except Exception as e:
            self.logger.debug(e)
            environ['is_authenticated'] = False
            return self.app(environ, start_response)
