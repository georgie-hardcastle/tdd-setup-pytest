from lib.greet import greet

def test_greet_returns_greeting():
    result = greet("Tester")
    assert result == "Hello, Tester!"