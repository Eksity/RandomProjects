from um import count
def test_normal():
    assert count("um") == 1
    assert count("um um um") == 3
    assert count("yum, um, umy... um") == 2

def test_words():
    assert count("yummy") == 0
    assert count("stumacx umy") == 0

def test_num():
    assert count("1um2") == 0
    assert count("1um") == 0

def test_case():
    assert count("Um,") == 1