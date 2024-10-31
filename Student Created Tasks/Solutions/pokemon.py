# Task 1
class Pokemon():
    def __init__(self, name, poke_type, attack_dmg, block_pts, attack_multi):
        self.name = name
        self.poke_type = poke_type
        self.attack_dmg = attack_dmg
        self.block_pts = block_pts
        self.attack_multi = attack_multi

    def display_info(self):
        print(f'''Hi! I am {self.name}!
My type is {self.poke_type}.
My attack and block points are {self.attack_dmg} and {self.block_pts} respectively.
My attack multiplier is {self.attack_multi}''')

    def attack(self, attacked_pokemon):
        types = ["Fire", "Ice", "Ground", "Electric", "Water"]
        # value of the type of pokemon of this object
        type_val1 = types.index(self.type)
        # value of type of attacked_pokemon
        type_val2 = types.index(attacked_pokemon.type)

        if type_val2 == 0:
            type_val2 = 5

        # check if pokemon type is "stronger"
        if type_val2 > type_val1:
            dmg = self.dmg * self.attack_multi

        else:
            dmg = self.dmg

        # subtract block pts
        dmg -= attacked_pokemon.block_pts


# Task 2
import csv


pokemon_list = []
# file closes after with block
with open("pokemon.txt", "r") as file:
    reader = csv.reader(file)
    # skip header
    next(reader)
    
    for row in reader:
        pokemon_list.append(Pokemon(row[0], row[1], int(row[2]), int(row[3]), float(row[4]))

# sort by poke_type
n = len(pokemon_list)
    
for i in range(n - 1, 0, -1):
    j = i - 1
    key = pokemon_list[i]
    while j >= 0 and key.type < pokemon_list[j].type:
        # shift element
        pokemon_list[j + 1] = pokemon_list[j]
        # check next element
        j -= 1

    # insert key into correct index
    pokemon_list[j + 1] = key

# sort by attack_dmg
for i in range(n):
    swapped = False
    for j in range(n - i - 1):
        if pokemon_list[j].attack_dmg > pokemon_list[j + 1].attack_dmg:
            # swap
            pokemon_list[j], pokemon_list[j + 1] = pokemon_list[j + 1], pokemon_list[j]
            swapped = True

    if not swapped:
        break

# print details
for pokemon in pokemon_list:
    print("-" * 15)
    print("Next Pokemon:")
    pokemon.display_info()
