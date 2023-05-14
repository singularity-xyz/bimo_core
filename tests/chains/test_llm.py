from chains import LLMChain
from utils import set_openai_api_key

# Set OPENAI_API_KEY environment variable
set_openai_api_key()

def test_llm_chain():
    chain = LLMChain()
    message = "Hello. This is a test."
    response = chain.run(message)

    assert isinstance(response, str)
    assert len(response) > 0

    print("Test: LLMChain()")
    print("Message:", message)
    print("Response:", response)