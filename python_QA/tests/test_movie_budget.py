import pytest

from movie_budget import calculate_movie_budget


def is_valid_budget(budget):
    return isinstance(budget, (int, float)) and budget > 0


def is_valid_crew_members(crew):
    return isinstance(crew, int) and crew > 0


def is_valid_costume_price(costumes):
    return isinstance(costumes, (int, float)) and costumes > 0


def is_valid_director_name(director: str) -> bool:
    if not isinstance(director, str) or not director.strip():
        return False
    allowed = set(" -'")  # spaces, hyphen, apostrophe
    return all(ch.isalpha() or ch in allowed for ch in director)


def is_valid_movie_name(movie: str) -> bool:
    if not isinstance(movie, str) or not movie.strip():
        return False
    # Movies can include letters, numbers, spaces, apostrophes, hyphens, and colons (e.g. "Spider-Man 2: Homecoming")
    allowed = set(" -':0123456789")
    return all(ch.isalpha() or ch in allowed for ch in movie)

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

# --Successful Crew Member Test Cases--


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

# --Successful Costume Test Cases--


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

# --Successful Director Name Test Cases


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
    assert is_valid_director_name(director) is True


def test_mb_24_director_spaces():
    # Arrange
    director = " John  Smith "
    # Act & Assert
    assert is_valid_director_name(director) is True


# --Movie Name successful Test Cases--


def test_mb_25_movie_one_word():
    # Arrange
    movie = "Accountant"
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_26_movie_leading_space():
    # Arrange
    movie = " Accountant"
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_27_movie_tailing_space():
    # Arrange
    movie = "Accountant "
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_28_movie_two_words():
    # Arrange
    movie = "The Accountant"
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_29_movie_multiple_spaces():
    # Arrange
    movie = "The  Accountant"
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_30_movie_hyphen():
    # Arrange
    movie = "The Diary of Anne-Marie"
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_31_movie_apostrophe():
    # Arrange
    movie = "The Life of Henry O'Brian"
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_32_movie_cyrillic():
    # Arrange
    movie = "Оркестър Без Име"
    # Act & Assert
    assert is_valid_movie_name(movie) is True


def test_mb_33_movie_spaces():
    # Arrange
    movie = " The  Accountant "
    # Act & Assert
    assert is_valid_movie_name(movie) is True

# --Unsuccessful Budget Test Cases--


def test_mb_34_budget_blank():
    # Arrange
    budget = ""
    # Act & Assert
    assert is_valid_budget(budget) is False


def test_mb_35_budget_zero():
    # Arrange
    budget = "0"
    # Act & Assert
    assert is_valid_budget(budget) is False


def test_mb_36_budget_negative_integer():
    # Arrange
    budget = "-123"
    # Act & Assert
    assert is_valid_budget(budget) is False


def test_mb_37_budget_negative_float():
    # Arrange
    budget = "-34.9807"
    # Act & Assert
    assert is_valid_budget(budget) is False


def test_mb_38_budget_text():
    # Arrange
    budget = "Two hundred thousand"
    # Act & Assert
    assert is_valid_budget(budget) is False


def test_mb_39_budget_character():
    # Arrange
    budget = "$500"
    # Act & Assert
    assert is_valid_budget(budget) is False


def test_mb_40_budget_space():
    # Arrange
    budget = " "
    # Act & Assert
    assert is_valid_budget(budget) is False

# --Unsuccessful Crew Test Cases--


def test_mb_41_crew_blank():
    # Arrange
    crew = ""
    # Act & Assert
    assert is_valid_crew_members(crew) is False


def test_mb_42_crew_space():
    # Arrange
    crew = " "
    # Act & Assert
    assert is_valid_crew_members(crew) is False


def test_mb_43_crew_zero():
    # Arrange
    crew = "0"
    # Act & Assert
    assert is_valid_crew_members(crew) is False


def test_mb_44_crew_float():
    # Arrange
    crew = "3.49"
    # Act & Assert
    assert is_valid_crew_members(crew) is False


def test_mb_45_crew_negative_integer():
    # Arrange
    crew = "-15"
    # Act & Assert
    assert is_valid_crew_members(crew) is False


def test_mb_46_crew_negative_float():
    # Arrange
    crew = "-24.65"
    # Act & Assert
    assert is_valid_crew_members(crew) is False


def test_mb_47_crew_text():
    # Arrange
    crew = "Hundred and twenty five"
    # Act & Assert
    assert is_valid_crew_members(crew) is False


def test_mb_48_crew_char():
    # Arrange
    crew = "$55.99"
    # Act & Assert
    assert is_valid_crew_members(crew) is False

# -- Unsuccessful Costume Test Cases


def test_mb_49_costume_blank():
    # Arrange
    costume = ""
    # Act & Assert
    assert is_valid_costume_price(costume) is False


def test_mb_50_costume_space():
    # Arrange
    costume = " "
    # Act & Assert
    assert is_valid_costume_price(costume) is False


def test_mb_51_costume_zero():
    # Arrange
    costume = "0"
    # Act & Assert
    assert is_valid_costume_price(costume) is False


def test_mb_52_costume_negative_integer():
    # Arrange
    costume = "-29"
    # Act & Assert
    assert is_valid_costume_price(costume) is False


def test_mb_53_costume_negative_float():
    # Arrange
    costume = "341.29"
    # Act & Assert
    assert is_valid_costume_price(costume) is False


def test_mb_54_costume_text():
    # Arrange
    costume = "Fifty five"
    # Act & Assert
    assert is_valid_costume_price(costume) is False


def test_mb_55_costume_char():
    # Arrange
    costume = "$444.44"
    # Act & Assert
    assert is_valid_costume_price(costume) is False

# -- Unsuccessful Director Name Test Cases


def test_mb_56_director_blank():
    # Arrange
    director = ""
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_57_director_space():
    # Arrange
    director = " "
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_58_director_integer():
    # Arrange
    director = "123"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_59_director_float():
    # Arrange
    director = "20.02"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_60_director_email():
    # Arrange
    director = "Adam@Calvin.com"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_61_director_mixed():
    # Arrange
    director = "Brian123"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_62_director_second_mixed():
    # Arrange
    director = "George$Michael432"
    # Act & Assert
    assert is_valid_director_name(director) is False

# --Unsuccessful Movie Name Test Cases--


def test_mb_63_movie_blank():
    # Arrange
    director = ""
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_64_movie_space():
    # Arrange
    director = " "
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_65_movie_integer():
    # Arrange
    director = "123"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_66_movie_float():
    # Arrange
    director = "12.36"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_67_movie_char():
    # Arrange
    director = "The Movie & Show"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_68_movie_mixed():
    # Arrange
    director = "7 Samurai Battle"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_69_movie_email():
    # Arrange
    director = "movie@gmail.com"
    # Act & Assert
    assert is_valid_director_name(director) is False


def test_mb_70_movie_mixed_second():
    # Arrange
    director = "Henry the 8th %89"
    # Act & Assert
    assert is_valid_director_name(director) is False

# --Successful Business Logic Test Cases--


def test_mb_71_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 100
    costume_price = 100
    director_name = "Wingard"
    movie_name = "Epic Battle"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Wingard starts filming 'Epic Battle' with 8000.00 leva left."
    assert difference == 8000.00


def test_mb_72_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 140
    costume_price = 100
    director_name = "Copolla"
    movie_name = "Good Boys"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Copolla starts filming 'Good Boys' with 4000.00 leva left."
    assert difference == 4000.00


def test_mb_73_business_logic_successful():
    # Arrange
    budget = 18000
    crew_members = 100
    costume_price = 140
    director_name = "Cem Yilmaz"
    movie_name = "GORA"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert f"Action! {director_name} starts filming {movie_name} with {difference} leva left."
    assert difference == 2200.00


def test_mb_74_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 100
    costume_price = 80
    director_name = "George Orwel"
    movie_name = "Animal Farm"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! George Orwel starts filming '1984' with 10000.00 leva left."
    assert difference == 10000.00


def test_mb_75_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 60
    costume_price = 120
    director_name = "Wingard"
    movie_name = "Epic Battle"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Wingard starts filming 'Epic Battle' with 10800.00 leva left."
    assert difference == 10800.00


def test_mb_76_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 150
    costume_price = 100
    director_name = "Nolan"
    movie_name = "Interstellar"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Nolan starts filming 'Interstellar' with 3000.00 leva left."
    assert difference == 3000.00


def test_mb_77_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 151
    costume_price = 100
    director_name = "Nolan"
    movie_name = "Interstellar"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Nolan starts filming 'Interstellar' with 4410.00 leva left."
    assert difference == 4410.00


def test_mb_78_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 200
    costume_price = 100
    director_name = "Nolan"
    movie_name = "Interstellar"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Nolan starts filming 'Interstellar' with 0.00 leva left."
    assert difference == 0.00


def test_mb_79_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 300
    costume_price = 15
    director_name = "Ridley Scot"
    movie_name = "Gladiator"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Ridley Scot starts filming 'Gladiator' with 13950.00 leva left."
    assert difference == 13950.00


def test_mb_80_business_logic_successful():
    # Arrange
    budget = 20000
    crew_members = 50
    costume_price = 350
    director_name = "Mel Gibson"
    movie_name = "The Braveheart"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Action! Mel Gibson starts filming 'The Braveheart' with 500.00 leva left."
    assert difference == 500.00


def test_mb_81_business_logic_successful():
    # Arrange
    budget = 10000
    crew_members = 100
    costume_price = 100
    director_name = "Gibbon"
    movie_name = "Epic War"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Not enough money! Gibbon needs 1000.00 leva more for 'Epic War'."
    assert difference == 1000.00


def test_mb_82_business_logic_successful():
    # Arrange
    budget = 5000
    crew_members = 100
    costume_price = 100
    director_name = "Cohen"
    movie_name = "Borat"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Not enough money! Cohen needs 5500.00 leva more for 'Borat'."
    assert difference == 5500.00


def test_mb_83_business_logic_successful():
    # Arrange
    budget = 2000
    crew_members = 50
    costume_price = 50
    director_name = "Mel Gibson"
    movie_name = "The Patriot"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Not enough money! Mel Gibson needs 700.00 leva more for 'The Patriot'."
    assert difference == 700.00


def test_mb_84_business_logic_successful():
    # Arrange
    budget = 5000
    crew_members = 100
    costume_price = 99.99
    director_name = "Nolan"
    movie_name = "Batman Begins"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Not enough money! Nolan needs 5499.00 leva more for 'Batman Begins'."
    assert difference == 5499.00


def test_mb_85_business_logic_successful():
    # Arrange
    budget = 4000
    crew_members = 99
    costume_price = 59.99
    director_name = "Scot"
    movie_name = "Napoleon"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is True
    assert "Not enough money! Scot needs 2339.01 leva more for 'Napoleon'."
    assert difference == 2339.01


def test_mb_86_business_logic_unsuccessful():
    # Arrange
    budget = 4000
    crew_members = 99.99
    costume_price = 60
    director_name = "Puso"
    movie_name = "The Godfather"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is False
    assert "Invalid input type. Please enter numbers where required."


def test_mb_87_business_logic_unsuccessful():
    # Arrange
    budget = 2000
    crew_members = 0
    costume_price = 10
    director_name = "Cameron"
    movie_name = "Avatar"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is False
    assert "Invalid input type. Please enter numbers where required."


def test_mb_88_business_logic_unsuccessful():
    # Arrange
    budget = 1000
    crew_members = -100
    costume_price = 100
    director_name = "Nolan"
    movie_name = "Memento"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is False
    assert "Invalid input type. Please enter numbers where required."


def test_mb_89_business_logic_unsuccessful():
    # Arrange
    budget = 1000
    crew_members = 100
    costume_price = 100
    director_name = ""
    movie_name = "Nemo"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is False
    assert "Invalid input type. Please enter numbers where required."


def test_mb_90_business_logic_unsuccessful():
    # Arrange
    budget = 1000
    crew_members = 100
    costume_price = 100
    director_name = " "
    movie_name = "Nemo2"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is False
    assert "Invalid input type. Please enter numbers where required."


def test_mb_91_business_logic_unsuccessful():
    # Arrange
    budget = 1000
    crew_members = 100
    costume_price = 100
    director_name = "123"
    movie_name = "Nemo3"
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is False
    assert "Invalid input type. Please enter numbers where required."


def test_mb_92_business_logic_unsuccessful():
    # Arrange
    budget = 1000
    crew_members = 100
    costume_price = 100
    director_name = "Buttler"
    movie_name = ""
    # Act
    valid, message, difference = calculate_movie_budget(
        budget, crew_members, costume_price, director_name, movie_name
    )
    # Assert
    assert valid is False
    assert "Invalid input type. Please enter numbers where required."


