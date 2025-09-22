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
    # Arrange
    crew = 222
    # Act & Assert
    assert is_valid_crew_members(crew) is True


def test_mb_09_crew_integer_low():
    # Arrange
    crew = 2
    # Act & Assert
    assert is_valid_crew_members(crew) is True


def test_mb_10_costume_integer_medium():
    # Arrange
    costume = 150
    # Act & Assert
    assert is_valid_costume_price(costume) is True


def test_mb_11_costume_float_medium():
    # Arrange
    costume = 123.34
    # Act & Assert
    assert is_valid_costume_price(costume) is True


def test_mb_12_costume_integer_low():
    # Arrange
    costume = 60
    # Act & Assert
    assert is_valid_costume_price(costume) is True


def test_mb_13_costume_float_low():
    # Arrange
    costume = 44.59
    # Act & Assert
    assert is_valid_costume_price(costume) is True


def test_mb_14_costume_integer_high():
    # Arrange
    costume = 469
    # Act & Assert
    assert is_valid_costume_price(costume) is True


def test_mb_15_costume_float_high():
    # Arrange
    costume = 625.12
    # Act & Assert
    assert is_valid_costume_price(costume) is True


def test_mb_16_director_first_name():
    # Arrange
    director = "John"
    # Act & Assert
    assert is_valid_director_name(director) is True


def test_mb_17_director_first_and_last_names():
    # Arrange
    director = "John Smith"
    # Act & Assert
    assert is_valid_director_name(director) is True


def test_mb_18_director_with_hyphen():
    # Arrange
    director = "Anne-Marie Muller"
    # Act & Assert
    assert is_valid_director_name(director) is True


def test_mb_19_director_with_apostrophe():
    # Arrange
    director = "Henry O'Brian"
    # Act & Assert
    assert is_valid_director_name(director) is True


def test_mb_20_director_with_name_tailing():
    # Arrange
    director = "John "
    # Act & Assert
    assert is_valid_director_name(director) is True


def test_mb_21_director_with_name_leading():
    # Arrange
    director = " John"
    # Act & Assert
    assert is_valid_director_name(director) is True


def test_mb_22_director_with_space_between():
    # Arrange
    director = "John  Smith"
    # Act & Assert
    assert is_valid_director_name(director) is True


def test_mb_23_director_cyrillic():
    # Arrange
    director = "Димитър Иванов"
    # Act & Assert
    assert is_valid_director_name(director)


def test_mb_24_director_spaces():
    # Arrange
    director = " John  Smith "
    # Act & Assert
    assert is_valid_director_name(director)


# --Movie Name successful Test Cases--


def test_mb_25_movie_one_word():
    # Arrange
    movie = "Accountant"
    # Act & Assert
    assert is_valid_movie_name(movie)


def test_mb_26_movie_leading_space():
    movie = " Accountant"
    assert is_valid_movie_name(movie)