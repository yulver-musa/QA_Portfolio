import pytest

from architect_hours import calculate_hours


def is_valid_name(name):
    return name.strip() != "" and name.strip().replace(" ", "").isalpha()


def is_valid_project_count(count_str):
    if count_str == "-0":
        return True
    return count_str.isdigit()


# --Successful Name Test Cases--

def test_ah_01_name_John():
    # Arrange
    name = "John"
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3

def test_ah_02_name_John_trailing():
    # Arrange
    name = "John "
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3

def test_ah_03_name_John_Anderson():
    # Arrange
    name = "John Anderson"
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3

def test_ah_04_name_John_Anderson_trailing():
    # Arrange
    name = "John Anderson "
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3

def test_ah_05_name_John_Anderson_leading():
    # Arrange
    name = " John Anderson"
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3

# --Successful Count Test Cases--

def test_ah_10_project_count_zero():
    project_count = "0"
    assert is_valid_project_count(project_count) is True
    assert calculate_hours(int(project_count)) == 0
