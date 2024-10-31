# Task 1.1
import random

def generate_2d_list():
    num_colors = int(input("Enter the number of colors: "))
    # Validation for perfect square number of colors
    while not (9 <= num_colors <= 100 and (num_colors ** 0.5).is_integer()):
        print("Please enter a perfect square number between 9 and 100.")
        num_colors = int(input("Enter the number of colors: "))

    # Create the grid accordingly
    grid = []
    for _ in range(num_colors):
        row = []
        for _ in range(3):
            row.append(random.randint(0, 255))
        grid.append(row)
    return grid

# Generate the 2-D list
grid = generate_2d_list()

# Print the generated 2-D list
for row in grid:
    print(row)

# Task 1.2
def den_to_hex(num):
    hex_digits = '0123456789abcdef'
    hex_str = ''
    
    while num > 0:
        remainder = num % 16
        hex_str = hex_digits[remainder] + hex_str
        num = num // 16
    
    # Ensure the hex string is two characters long
    if len(hex_str) == 0:
        hex_str = '00'
    elif len(hex_str) == 1:
        hex_str = '0' + hex_str
    
    return hex_str

# Apply den_to_hex to the 2-D list and print it line by line
hex_grid = [[den_to_hex(num) for num in row] for row in grid]

# Convert hex_grid to the desired format
formatted_hex_grid = []
for row in hex_grid:
    formatted_row = '#' + ''.join(row)
    formatted_hex_grid.append(formatted_row)

# Task 1.3
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Apply merge sort to formatted_hex_grid
merge_sort(formatted_hex_grid)
print(formatted_hex_grid)
