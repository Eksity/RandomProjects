from numb3rs import validate

def test_normal():
    assert validate("19.38.42.12") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_big():
    assert validate("257.352.12.12") == False
    assert validate("1.1.1.256") == False

def test_letters():
    assert validate("19.38.42.cat") == False
    assert validate("cat") == False