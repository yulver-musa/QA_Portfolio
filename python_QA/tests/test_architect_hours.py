import pytest

from architect_hours import calculate_hours

def test_calculate_hours():
    assert calculate_hours(4) == 12