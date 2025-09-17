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
    # Act&Assert
    assert is_valid_budget(budget) is True
