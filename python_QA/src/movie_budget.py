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
        not director_name.replace(" ", "").replace("-", "").replace("'", "").isalpha() or
        not isinstance(movie_name, str) or not movie_name.strip() or
        not movie_name.replace(" ", "").replace("-", "").replace("'", "").isalpha()
    ):
        return False, "Invalid input data provided.", None

    # --- Business logic ---
    decor = movie_budget * 0.1

    if crew_members > 150:
        costume_price *= 0.9

    total_costumes = crew_members * costume_price
    total_expenditures = total_costumes + decor

    # --- Calculation ---
    difference = round(movie_budget - total_expenditures, 2)

    if movie_budget >= total_expenditures:
        message = f"Action {director_name} starts filming '{movie_name}' with " \
                  f"{difference:.2f} leva left."
    else:
        message = f"Not enough money! {director_name} needs {difference:.2f} leva more for '{movie_name}'."

    return True, message, difference


def main():
    try:
        movie_budget = float(input("Enter movie budget: "))
        crew_members = int(input("Enter number of crew members: "))
        costume_price = float(input("Enter costume price: "))
        director_name = input("Enter director's name: ")
        movie_name = input("Enter movie name: ")

        valid, message, difference = calculate_movie_budget(
            movie_budget, crew_members, costume_price, director_name, movie_name
        )
        print(message)
    except ValueError:
        print("Invalid input type. Please enter numbers where required.")


if __name__ == "__main__":
    main()
