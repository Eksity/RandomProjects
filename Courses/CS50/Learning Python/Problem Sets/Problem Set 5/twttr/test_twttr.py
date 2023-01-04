from twttr import shorten

def test_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AeIoU") == ""

def test_letters_only():
    assert shorten("the quick brown fox jumps over the lazy dog") == "th qck brwn fx jmps vr th lzy dg"

def test_letters_and_numbers():
    assert shorten("a1b2c3d4e5f6") == "1b2c3d45f6"

def test_punctuation():
    assert shorten("this, is! a. test$") == "ths, s! . tst$"
