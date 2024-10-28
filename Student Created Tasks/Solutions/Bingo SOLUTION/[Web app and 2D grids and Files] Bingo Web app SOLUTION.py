# Task 1.1
import csv

# Generates 25 unique numbers from 1 to 75
numbers = random.sample(range(1, 75), 25)

# Changes list 'numbers' into a 5x5 2D list
grid = []
for i in range(5):
    row = numbers[i*5:(i+1)*5]  # splicing in groups of 5
    grid.append(row)

# Set the center square (3rd row, 3rd column) to 'Free'
grid[2][2] = 'Free'

# Storing and extracting grid
# Method 1: csv (easier)
#file closes after with block
with open("BINGO.txt", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grid)

# Extracting grid
#file closes after with block
with open("BINGO.txt", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
# Method 2: using normal python (alternative)
#file closes after with block
with open("BINGO.txt", "w") as file:
    for line in grid:
        file.write(", ".join(line) + "\n")

# Extracting grid
#file closes after with block
with open("BINGO.txt", "r") as file:
    for line in file:
        print(line.rstrip().split(", "))


# Task 1.2
import random
import csv

# Extract grid frome TEST.txt
#file closes after with block
with open("TEST.txt", "r") as file:
    reader = csv.reader(file)
    grid = []
    for row in reader:
        converted_row = [int(char) if char.isdigit() else char for char in row]  # converts all numbers from string into integers

        #alternative method
        converted_row = []
        for char in row:
            if char.isdigit():
                converted_row.append(int(char))
            else:
                converted_row.append(char)
        grid.append(converted_row)

# creation of bingo(grid) function
def bingo(grid):
    chosen_numbers = []
    complete = False

    while not complete:
        user_input = input("Enter 'Next' to generate a number or 'End' to end the game: ").strip().lower() # removes excess white space and standardise input
        
        if user_input == 'next':
            num = random.randint(1, 75) # picks random number from 1 to 75
            while num in chosen_numbers: # checks if number has already been chosen
                num = random.randint(1, 75)
            chosen_numbers.append(num)    
            print(f"Generated number: {num}")
        
        elif user_input == 'end':
            for row in range(5):
                for col in range(5):
                    if row == 2 and col == 2:  # free space is always True
                        grid[row][col] == True
                    elif grid[row][col] in chosen_numbers:  # if number has been chosen, replace with True
                        grid[row][col] = True
                    else:
                        grid[row][col] = False

            complete = True # breaks loop

    for row in grid: #prints new grid
                print(row)

# Test
bingo(grid)


# Task 1.3

#create function to check if all true
def consec_true(bool1, bool2, bool3, bool4, bool5):
    return bool1 and bool2 and bool3 and bool4 and bool5

def grid_check(grid):
    # Check rows
    for row in grid:
        if consec_true(row[0], row[1], row[2], row[3], row[4]):
            return True
    
    # Check columns
    for col in range(5):
        if consec_true(grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col]):
            return True
    
    # Check diagonals
    if consec_true(grid[0][0], grid[1][1], grid[2][2], grid[3][3], grid[4][4]) or consec_true(grid[4][0], grid[3][1], grid[2][2], grid[1][3], grid[0][4]):
        return True
    
    return False

# Test the function
grid1 = [  # Output should be False
    [True, True, False, True, True],
    [False, False, False, False, False],
    [False, True, True, True, False],
    [False, True, True, True, True],
    [True, False, True, True, True],
]

grid2 = [  # Output should be True
    [True, True, True, True, True],
    [False, False, False, False, False],
    [False, True, True, True, False],
    [False, True, True, True, True],
    [True, True, True, True, True],
]

print(grid_check(grid1), grid_check(grid2))