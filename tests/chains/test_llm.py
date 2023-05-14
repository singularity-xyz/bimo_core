from chains import LLMChain

def test_llm():
    chain = LLMChain()
    message = "This is a test. Please respond with 'Hello World!'."
    response = chain.run(message)

    assert isinstance(response, str)
    assert len(response) > 0
    assert response == "Hello World!"

    print("Message:", message)
    print("Response:", response)
