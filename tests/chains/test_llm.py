import pytest
from chains import LLMChain
from utils import logging

@pytest.mark.parametrize("message,expected_response", [
    ("This is a test. Please respond with 'Hello World!'.", "Hello World!"),
])
def test_llm(message, expected_response):
    chain = LLMChain()
    response = chain.run(message)

    assert isinstance(response, str)
    assert len(response) > 0
    assert response == expected_response

    print() # for cleaner output
    logging.info("Message: %s", message)
    logging.info("Response: %s", response)
