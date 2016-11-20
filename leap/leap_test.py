import pytest
from leap import is_leap_year


def test_leap_year():
    assert is_leap_year(1996) is True


def test_non_leap_year():
    assert is_leap_year(1997) is False


def test_non_leap_even_year():
    assert is_leap_year(1998) is False


def test_century():
    assert is_leap_year(1900) is False


def test_exceptional_century():
    assert is_leap_year(2400) is True


if __name__ == '__main__':
    pytest.main()
