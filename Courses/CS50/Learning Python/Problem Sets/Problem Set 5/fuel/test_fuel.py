from fuel import convert, gauge
import pytest

def test_convert_normal():
    assert convert("1/4") == 25
    assert convert("2/5") == 40

def test_convert_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("12/0")

def test_convert_xy():
    with pytest.raises(ValueError):
        convert("43/21")

def test_gauge_normal_full_empty():
    assert gauge(57) == "57%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

