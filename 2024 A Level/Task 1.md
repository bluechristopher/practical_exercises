>Name your Jupyter Notebook as:
>
>`TASK1_<your name>_<centre number>_<index number>.ipynb`


# Task 1

A game designer is designing a game for 2 players and needs you to program a prototype.

Players in the game have 10 randomly generated cards. This is called a 'hand'. The cards each have a colour (red, green or blue) and a number (1, 2, 3 or 4). There is no limit to the number of copies of each card, for example, there can be multiple cards that are red and 1. Each player has a score that is 0 when the game starts.

In this prototype, the cards will be randomly generated for each player and sorted into ascending order by number.

On each turn:
- The next card from Player 1's hand is selected.
- The next card from Player 2's hand is selected.
- These 2 cards are compared.

The winning card is determined based on the colour of each card:
- A red card wins over a green card.
- A green card wins over a blue card.
- A blue card wins over a red card.

The number on the winning card is multiplied by 2. This value is then added to the score of the player who had the winning card.

The number on the losing card is added to the score of the player who had the losing card.

If both colours are the same:
- Player 1's card number is added to player 1's score.
- Player 2's card number is added to player 2's score.

For each of the sub-tasks, add a comment statement at the beginning of the code, using the hash symbol `#`, to indicate the sub-task the program code belongs to, for example:

<pre>
# Task 1.1
Program code
</pre>

## Task 1.1

Write a program to set up the game for 2 players by:
- creating a list for each player
- randomly generating 10 cards (each with a colour and number) to each player's list.

[4]

Test your program by outputting the contents of each player's hand.

[1]

---

## Task 1.2

Write a function that takes the colour of two cards as parameters and returns the result of the comparison. The function should return '1' if the first colour wins, '2' if the second colour wins and '3' if the colours are the same.

[2]

---

## Task 1.3

The cards in each hand now need to be sorted into numerical order.

Write a function to take a hand as a parameter, sort the hand in-place into ascending numerical order, and return the sorted hand. If two cards have the same number, the colours are compared to position the cards in this order: red, green, blue.

Call the function to sort each of the 2 players' hands. Output the contents of each hand before and after sorting. The contents of a hand must be output on one line.

Do not use a built-in sorting function.

[8]

---

## Task 1.4

The cards are compared in pairs, starting with the first card from player 1 compared to the first card from player 2.

The appropriate numbers are added to each player's score until all of the 10 cards have been used.

Write a function to calculate and return the final score for each of the 2 players.

[5]

Test your program by:
- outputting the sorted hand and the final score for player 1 on one line
- outputting the sorted hand and the final score for player 2 on one line.

[1]

---

## Task 1.5

Write a function to calculate and output which player has won (has the higher final score), and which player has come second.

There must be a suitable output if there is a draw.

All outputs must have an appropriate message.

[2]

Test your program.

[1]

Save your Jupyter Notebook for Task 1.




