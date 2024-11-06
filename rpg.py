import random #importing the random

CREATURES = ['monster', 'rabbit', 'fox', 'rat'] #creating the list of creatures
ITEMS = ['helmet', 'shield', 'boots', 'chest plate','gauntlets'] #creating the list of items
OTHER_ITEMS = ['bush', 'big tree', 'rock'] 
ALL_THINGS = CREATURES + ITEMS + OTHER_ITEMS

health = 20 #initializing the health to 20
coins = 0 #initial value of coin =0
lst = []

while True:
    print("\033[H\033[2J", end="") #clearing the screen
    print(f"Current Health = {health}, Coins = {coins}, Numofitems: {len(lst)}")
    for item in lst:
        print(item, end= " ")
    print()

    encounter = random.choice(ALL_THINGS)

    if encounter in ITEMS and encounter not in lst:
        ask= input(f"Do you want to take the {encounter}? (yes/no):")
        if ask.lower() != 'no':
            lst.append(encounter)
            print(f"You have taken the {encounter} ")

    elif encounter in CREATURES:
        if encounter == 'monster':
            if any(item in ITEMS for item in lst):
                attack_amount = 3 #less damage if player has armor
            else:
                attack_amount = 7 #more damage if player has armor

            print(f"A {encounter} attacks you for {attack_amount} damage!")
            health -= attack_amount

            if health <= 0:
                print(f"Your have lost the game as your health dropped to {health}")
                break
    attack = input(f"Do you want to fight the {encounter}? (y/n):")
    if attack.lower() != 'n':
        if encounter == 'monster':
            coins += 10
        else:
            coins += 1
        print(f"You have defeated the {encounter} and earned coins!") 

        #checking if the player has won the game
        if coins >= 100:
            print("Congratulations! You have won the game!")
            break

input("Please enter to keep walking")


















