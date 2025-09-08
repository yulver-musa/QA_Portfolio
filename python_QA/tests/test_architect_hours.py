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


def test_ah_06_name_John_Anderson_multiple():
    # Arrange
    name = "John   Anderson"
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3


def test_ah_07_name_Anne_Marie_Muller_dash():
    # Arrange
    name = "Anne-Marie Muller"
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3


def test_ah_08_name_Henry_O_Brian_apostrophe():
    # Arrange
    name = "Henry O'Brian"
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3


def test_ah_09_name_Dimitar_Ivanov_multiple():
    # Arrange
    name = "Димитър Иванов"
    # Act & Assert
    assert is_valid_name(name) is True
    assert calculate_hours(1) == 3


# --Successful Count Test Cases--

def test_ah_10_project_count_zero():
    # Arrange
    project_count = "0"
    # Act & Assert
    assert is_valid_project_count(project_count) is True
    assert calculate_hours(int(project_count)) == 0


def test_ah_11_project_count_five():
    # Arrange
    project_count = "5"
    # Act & Assert
    assert is_valid_project_count(project_count) is True
    assert calculate_hours(int(project_count)) == 15


def test_ah_12_project_count_thirteen():
    # Arrange
    project_count = "13"
    # Act & Assert
    assert is_valid_project_count(project_count) is True
    assert calculate_hours(int(project_count)) == 39



def test_ah_13_project_count_twentyone():
    # Arrange
    project_count = "21"
    assert is_valid_project_count(project_count) is True
    assert calculate_hours(int(project_count)) == 63


def test_ah_14_project_count_hundredtwentyfive():
    # Arrange
    project_count = "125"
    assert is_valid_project_count(project_count) is True
    assert calculate_hours(int(project_count)) == 375


def test_ah_15_project_count_minuszero():
    # Arrange
    project_count = "-0"
    assert is_valid_project_count(project_count) is True
    assert calculate_hours(int(project_count)) == 0

# --Unsuccessful Name Test Cases--

def test_ah_16_project_name_emptyspace():
    # Arrange
    name = " "
    # Act & Assert
    assert is_valid_name(name) is False
    assert calculate_hours(1) == 3

def test_ah_17_project_name_blank():
    # Arrange
    name = ""
    # Act & Assert
    assert is_valid_name(name) is False
    assert calculate_hours(1) == 3

def test_ah_18_project_name_textandinteger():
    # Arrange
    name = "John123"
    # Act & Assert
    assert is_valid_name(name) is False
    assert calculate_hours(1) == 3


def test_ah_19_project_name_integer():
    # Arrange
    name = "1234"
    # Act & Assert
    assert is_valid_name(name) is False
    assert calculate_hours(1) == 3


def test_ah_20_project_name_textwithcharandinteger():
    # Arrange
    name = "Jo$n1234"
    # Act & Assert
    assert is_valid_name(name) is False
    assert calculate_hours(1) == 3


def test_ah_21_project_name_textwithblankandchar():
    # Arrange
    name = "John @Dollar"
    # Act & Assert
    assert is_valid_name(name) is False
    assert calculate_hours(1) == 3


def test_ah_22_project_name_email():
    # Arrange
    name = "John.dollar@test.io"
    # Act & Assert
    assert is_valid_name(name) is False
    assert calculate_hours(1) == 3


# --Unsuccessful Count Test Cases--


def test_ah_23_project_count_float():
    # Arrange
    project_count = "6.5"
    # Act & Assert
    assert is_valid_project_count(project_count) is False