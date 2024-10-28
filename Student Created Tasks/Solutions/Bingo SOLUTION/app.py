from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

bingo_cards = {} # Dictionary of bingo cards
chosen_numbers = []
players_count = 0

def create_card():  # from task 1.1
    numbers = random.sample(range(1, 76), 25)
    card = [numbers[i * 5:(i + 1) * 5] for i in range(5)]
    card[2][2] = "Free"  # Center square
    return card

def consec_true(bool1, bool2, bool3, bool4, bool5):
    return bool1 and bool2 and bool3 and bool4 and bool5

def grid_check(grid):  #from task 1.3
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

@app.route('/', methods=['GET', 'POST'])
def index():
    global players_count
    global chosen_numbers
    global bingo_cards
    chosen_numbers = [] #clears for next game
    bingo_cards = {}
    if request.method == 'POST':
        players_count = int(request.form.get('players'))
        # Create bingo cards for each player
        for i in range(players_count):
            bingo_cards[f'Player{i+1}'] = create_card()
        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    global chosen_numbers
    if request.method == 'POST':
        if request.form.get("generate"):  # if generate number button was pressed
            num = random.randint(1, 75) # from task 1.2
            while num in chosen_numbers:
                num = random.randint(1, 75)
            chosen_numbers.append(num)
            if len(chosen_numbers) >= 75: # Check if all numbers have appeared
                return render_template('game.html', cards=bingo_cards, number='Tie, no winners.')
            else:
                return render_template('game.html', cards=bingo_cards, number=num)
        elif request.form.get("end"):
            return redirect(url_for('check_bingo'))
    return render_template('game.html', cards=bingo_cards, number="")

@app.route('/check_bingo', methods=['GET', 'POST'])
def check_bingo():
    global bingo_cards
    if request.method == 'POST':
        winner = request.form.get('winner')
        grid = bingo_cards[winner] # finds winning card

        if grid_check(grid):
            return f"{winner} has Bingo!"
        else:
            return f"{winner} does not have Bingo."
    return render_template('check_bingo.html', players=bingo_cards.keys())

if __name__ == '__main__':
    app.run(debug=True, port=5000)