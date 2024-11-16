"""Entry points for the application."""
from typing import Dict, Union

import logging
import json

logger = logging.getLogger()
logger.setLevel('INFO')


def process(message: str) -> str:
    """Process message. The application logic is impleted here.
    Nothing to implement for the assessment.
    """
    return f"The received message is: '{message}'"


JSON = Dict[str, Union[int, str, float, 'JSON']]

LambdaEvent = JSON
LambdaContext = object
LambdaOutput = JSON


def lambda_handler(event: LambdaEvent, context: LambdaContext) -> LambdaOutput:  # noqa: ARG001
    """Entry point for Lambda function.

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    -------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html

    """

    if 'body' in event:  # Check if body exists in the event
        event_body = json.loads(event.get('body'))  # Load the json into a dict
        if 'message' in event_body:  # Check if message exists in the body
            statuscode = 200
            message = event_body['message']
        else:  # If message doesn't exists then error code and message
            message = 'There was no message'
            statuscode = 404
    else:  # If body doesn't exists then error code and message
        message = 'There was no body in the message'
        statuscode = 400

    returnbody = process(message)
    return {
        'statuscode': statuscode,
        'body': returnbody,
    }
