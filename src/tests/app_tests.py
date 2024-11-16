from app.app import lambda_handler, LambdaContext, LambdaEvent
import pytest


@pytest.mark.parametrize(
    "event,exptectedCode, expectedMessage",
    [({"body": "{\"message\": \"hello world\"}"}, 200, 'hello world'),
     ({"body": "{}"}, 404, "There was no message"),
     ({"head": "{\"message\": \"hello world\"}"}, 400, "There was no body in the message")],
)
def test_lambda_handler(event: LambdaEvent, exptectedCode, expectedMessage):
    returned = lambda_handler(event, LambdaContext)
    assert returned["statusCode"] == exptectedCode
    assert returned["body"] == f"The received message is: '{expectedMessage}'"
