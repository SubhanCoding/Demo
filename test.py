def read_numbers_from_file(filename):

    numbers = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(int(line))
    return numbers


def calculate_statistics(numbers):

    total = len(numbers)
    sum_values = sum(numbers)
    average = round(sum_values / total) if total > 0 else 0
    min_value = min(numbers)
    max_value = max(numbers)
    return total, sum_values, average, min_value, max_value


def display_statistics(total, sum_values, average, min_value, max_value):

    print(f"Total = {total}")
    print(f"Summation = {sum_values}")
    print(f"Average = {average}")
    print(f"Minimum = {min_value}")
    print(f"Maximum = {max_value}")


def compute_stats(filename):
    """Main function to execute the full process."""
    try:
        numbers = read_numbers_from_file(filename)
        total, sum_values, average, min_value, max_value = calculate_statistics(numbers)
        display_statistics(total, sum_values, average, min_value, max_value)
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data in file. Please ensure all lines are integers.")


if __name__ == "__main__":
    compute_stats("random_nums.txt")
