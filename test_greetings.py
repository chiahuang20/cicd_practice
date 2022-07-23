from main import greetings, num_add

def test_greetings():
    assert greetings('Steven') == 'Hello Steven!'

def test_num_add():
    assert num_add(3, 4) == 7