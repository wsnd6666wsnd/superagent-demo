from greet import greet


def test_greet_returns_hello_with_name() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_uses_given_name() -> None:
    assert greet("Alice") == "Hello, Alice!"
