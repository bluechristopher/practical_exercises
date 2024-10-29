# Task 1
A Pokemon() class has the following attributes
- name
- type
- attack_dmg (the attack damage)
- block_pts (the points of damage blocked when attacked)
- attack_multi (the attack multipler)

The class has a display_info() method that prints the attributes in an appropriate format.

The class also has a method attack(attacked_pokemon) where attacked_pokemon parameter is another pokemon object. 
The method reduces the health of the attacked_pokemon by the attack_dmg of the attacking pokemon minus the block_pts of the attacked pokemon.
However, if the type of attacking pokemon is 'stronger' than the type of the attacked pokemon, the attack_dmg will be multiplied by attack_multi of the attacking pokemon.

Below is a circular list of the pokemon types that are 'stronger' than the adjacent types to the right: 

["fire", "ice", "ground", "electric", "water"]

Create the Pokemon() class and add the constructor and the additional method. [5]

# Task 2
The file pokemon.txt contains rows of attributes from the Pokemon() class
- Read data from pokemon.txt
- Create a list of Pokemon objects
- Use insertion sort to sort the list by type
- Use bubble sort to sort the same list by attack_dmg
- Print the details of each pokemon in the sorted list using appropriate method(s) from the pokemon() class

Save your file.
