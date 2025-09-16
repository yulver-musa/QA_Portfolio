import pytest

from movie_budget import calculate_movie_budget


def is_valid_budget(budget):
    return isinstance(budget, (int, float)) and budget > 0