def calculate_hours(projects):
    """Calculate total hours for an architect."""
    hours_per_project = 3
    return projects * hours_per_project


import re


# Main program


def main():
    name_of_architect = input("Enter architect's name: ")
    if not re.fullmatch(r"[A-Za-z\s'-]+", name_of_architect):
        print("Error: Invalid name!")
        exit(1)

    count_of_projects_input = input("Enter number of projects: ")
    if not count_of_projects_input.isdigit():
        print("Error: Number of projects must be a non-negative integer!")
        exit(1)

    count_of_projects = int(count_of_projects_input)
    total_hours = calculate_hours(count_of_projects)

    print(f"The architect {name_of_architect} will need {total_hours} hours to complete {count_of_projects} project/s.")


if __name__ == "__main__":
    main()
