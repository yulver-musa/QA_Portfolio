def calculate_movie_budget(movie_budget, crew_members, costume_price, director_name,
                           movie_name):
    """

    Args:
        movie_budget (float): Total available budget for the movie. Must be > 0.
        crew_members (int): Number of crew members. Must be a positive integer.
        costume_price (float): Price per costume. Must be > 0.
        director_name (str): Name of the director (non-empty string).
        movie_name (str): Title of the movie (non-empty string).

    Returns:
        tuple:
            valid_input (bool): False if validation fails, True otherwise.
            message (str): Result message, e.g., "Action!" or "Not enough money!".
            difference (float or None): Budget difference.

    """


    # --- Input validation ---
