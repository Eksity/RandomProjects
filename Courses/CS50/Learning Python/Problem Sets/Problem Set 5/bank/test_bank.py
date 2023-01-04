from bank import value

def test_0s():
    assert value("hello") == 0
    assert value("HeLlO") == 0
    assert value(" hello ") == 0

def test_20s():
    assert value("henlo") == 20
    assert value("hyper") == 20
    assert value(" h ") == 20

def test_100s():
    assert value("beans") == 100
    assert value("") == 100
    assert value(" nkdslnb132312w.jkgn") == 100