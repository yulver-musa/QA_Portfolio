def calculate_hours(projects):
    """Calculate total hours for an architect."""
    hours_per_project = 3
    return projects * hours_per_project


# Main program
def is_valid_name(name_of_architect: str) -> bool:
    allowed = set(" -'")  # spaces, hyphens, apostrophes
    return bool(
        name_of_architect.strip()
        and all(ch.isalpha() or ch in allowed for ch in name_of_architect)
    )


def is_valid_project_count(count) -> bool:
    if isinstance(count, int):
        return count >= 0 or count == -0  # zero and negative zero are allowed

    if isinstance(count, str):
        if count == "0" or count == "-0":
            return True
        return count.isdigit()  # positive integers as string

    return False


def main():
    name_of_architect = input("Enter architect's name: ")
    if not is_valid_name(name_of_architect):
        print("Error: Name of the architect must contain letters only!")
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
