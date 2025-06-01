from allidatar import hello

def test_hello_default():
  assert hello() == "Hello, World!"

def test_hello_custom():
  assert hello("Alice") == "Hello, Alice!"
