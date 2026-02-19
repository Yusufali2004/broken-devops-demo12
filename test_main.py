from main import add_numbers

def test_add_numbers():
    # This will fail because 10 + 5 is not 50
    assert add_numbers(10, 5) == 15

def test_syntax():
    # This test won't even run until the syntax error in main.py is fixed
    assert True
