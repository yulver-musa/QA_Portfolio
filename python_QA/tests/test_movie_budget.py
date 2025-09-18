import pytest

from movie_budget import calculate_movie_budget


def is_valid_budget(budget):
    return isinstance(budget, (int, float)) and budget > 0


def is_valid_crew_members(crew):
    return isinstance(crew, int) and crew > 0


def is_valid_costume_price(costumes):
    return isinstance(costumes, (int, float)) and costumes > 0


def is_valid_director_name(director):
    return isinstance(director, str) and director.strip() != ""


def is_valid_movie_name(movie):
    return isinstance(movie, str) and movie.strip() != ""


# --Successful Budget Test Cases--


def test_mb_01_integer_high():
    # Arrange
    budget = 500000
    # Act & Assert
    assert is_valid_budget(budget) is True


def test_mb_02_float_high():
    # Arrange
    budget = 150000.15
    # Act & Assert
    assert is_valid_budget(budget) is True


def test_mb_03_integer_low():
    # Arrange
    budget = 20
    # Act & Assert
    assert is_valid_budget(budget) is True


def test_mb_04_float_low():
    # Arrange
    budget = 0.50
    # Act & Assert
    assert is_valid_budget(budget) is True


def test_mb_05_float_medium():
    # Arrange
    budget = 1234.65
    # Act & Assert
    assert is_valid_budget(budget) is True

def test_mb_06_float_medium():
    # Arrange
    budget = 999
    # Act & Assert
    assert is_valid_budget(budget) is True


def test_mb_07_crew_integer_medium():
    # Arrange
    crew = 12
    # Act & Assert
    assert is_valid_crew_members(crew) is True


def test_mb_08_crew_integer_high():

