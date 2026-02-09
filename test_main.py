import main

def test_add():
    assert main.add(3, 4) == 7
    assert main.add(5, 10) == 15
    assert main.add(-3, 4) == 1