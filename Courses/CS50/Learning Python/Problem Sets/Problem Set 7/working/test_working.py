import working
import pytest



def test_convert():
    assert working.convert("9 AM to 5 PM") == ("09:00 to 17:00")
    assert working.convert("1:34 AM to 2:56 PM") == ("01:34 to 14:56")

def test_outside():
    with pytest.raises(ValueError):
        working.convert("9AM to 5PM")

    with pytest.raises(ValueError):
        working.convert("9 am to 5 pm")

    with pytest.raises(ValueError):
        working.convert("13 AM to 15 PM")

def test_2digit():
    assert working.convert("12 AM to 11 PM") == ("00:00 to 23:00")

def test_omission():
    with pytest.raises(ValueError):
        working.convert("9AM 5PM")
