# Task 1.1
import random

def generate_2d_list():
    num_colors = int(input("Enter the number of colors: "))
    # Validation for perfect square number of colors
    while not (9 <= num_colors <= 100 and (num_colors ** 0.5).is_integer()):
        print("Please enter a perfect square number between 9 and 100.")
        num_colors = int(input("Enter the number of colors: "))

    # Create the grid accordingly
    return [[random.randint(0, 255) for _ in range(3)] for _ in range(num_colors)]

# Generate the 2-D list
grid = generate_2d_list()

# Print the generated 2-D list
for row in grid:
    print(row)