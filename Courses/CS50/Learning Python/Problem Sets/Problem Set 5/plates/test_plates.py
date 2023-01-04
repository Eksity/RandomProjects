import plates

def test_correct_length():
    assert plates.is_valid("A") == False
    assert plates.is_valid("AAAAAAAAAAAAA") == False

def test_correct_start():
    assert plates.is_valid("A3AAA") == False
    assert plates.is_valid("3AAAA") == False
    assert plates.is_valid("333") == False

def test_only_letters_and_numbers():
    assert plates.is_valid("AAA,AA") == False
    assert plates.is_valid("!!!!!") == False
    assert plates.is_valid("AA AA") == False

def test_correct_numbers():
    assert plates.is_valid("AA34AA") == False
    assert plates.is_valid("AAAA04") == False

def test_all_correct():
    assert plates.is_valid("AAAAA") == True
    assert plates.is_valid("NRVOUS") == True