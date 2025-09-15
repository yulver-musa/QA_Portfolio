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


    if (
        not isinstance(movie_budget, (int, float)) or movie_budget <= 0 or
        not isinstance(crew_members, int) or crew_members <= 0 or
        not isinstance(costume_price, (int, float)) or costume_price <= 0 or
        not isinstance(director_name, str) or not director_name.strip() or
        not isinstance(movie_name, str) or not movie_name.strip()
    ):
        return False, "Invalid input data provided.", None

    # --- Business logic ---
    decor = movie_budget * 0.1

    if crew_members > 150:
        costume_price *= 0.9

    total_costumes = crew_members * costume_price
    total_expenditures = total_costumes + decor

