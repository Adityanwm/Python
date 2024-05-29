import time

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious forest.")
    print("Your goal is to find the legendary treasure hidden deep within the forest.")
    print("But be warned, danger lurks around every corner.")
    print("Your fate is in your hands. Let the adventure begin!")
    time.sleep(2)
    input("Press Enter to continue...")

def forest_path():
    print("\nYou come across a fork in the path.")
    print("Do you go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == "left":
        print("\nYou chose the left path and encounter a group of friendly elves.")
        print("They offer to guide you deeper into the forest.")
        time.sleep(2)
        elven_village()
    elif choice == "right":
        print("\nYou chose the right path and encounter a ferocious bear!")
        print("You must fight or flee.")
        time.sleep(2)
        fight_or_flee()
    else:
        print("\nInvalid choice. Please try again.")
        forest_path()

def elven_village():
    print("\nYou arrive at the elven village and are greeted warmly by the inhabitants.")
    print("They tell you about a hidden cave where the treasure is rumored to be.")
    print("But to reach the cave, you must first pass through the Dark Forest.")
    print("The elves offer you a magical potion to protect you on your journey.")
    time.sleep(2)
    potion_choice()

def potion_choice():
    print("\nThe elves offer you two potions: a blue potion and a red potion.")
    choice = input("Which potion do you choose? (blue/red): ").lower()
    if choice == "blue":
        print("\nYou drink the blue potion and feel a surge of energy.")
        print("With renewed strength, you set off towards the Dark Forest.")
        time.sleep(2)
        dark_forest()
    elif choice == "red":
        print("\nYou drink the red potion and feel a sense of calm wash over you.")
        print("Feeling protected, you set off towards the Dark Forest.")
        time.sleep(2)
        dark_forest()
    else:
        print("\nInvalid choice. Please try again.")
        potion_choice()

def dark_forest():
    print("\nYou enter the Dark Forest, shrouded in darkness and mystery.")
    print("Suddenly, you hear a rustling in the bushes.")
    print("Do you investigate or continue on your path?")
    choice = input("Enter 'investigate' or 'continue': ").lower()
    if choice == "investigate":
        print("\nYou investigate the source of the rustling and find a hidden chest!")
        print("Inside the chest, you find valuable treasures.")
        print("Congratulations, you have found the legendary treasure!")
        time.sleep(2)
        game_over()
    elif choice == "continue":
        print("\nYou continue on your path through the forest.")
        print("The darkness seems to close in around you.")
        print("You feel a sense of unease, but press on.")
        time.sleep(2)
        print("\nSuddenly, you step into a clearing and find yourself face to face with a dragon!")
        print("Prepare for battle!")
        time.sleep(2)
        battle_with_dragon()
    else:
        print("\nInvalid choice. Please try again.")
        dark_forest()

def fight_or_flee():
    print("\nDo you fight the bear or flee?")
    choice = input("Enter 'fight' or 'flee': ").lower()
    if choice == "fight":
        print("\nYou bravely face the bear and engage in a fierce battle.")
        time.sleep(2)
        print("After a grueling fight, you emerge victorious!")
        print("You continue on your journey, heart pounding with adrenaline.")
        time.sleep(2)
        forest_path()
    elif choice == "flee":
        print("\nYou choose to flee from the bear and run as fast as you can.")
        print("You manage to escape, but your heart is racing.")
        print("You take a moment to catch your breath before continuing on.")
        time.sleep(2)
        forest_path()
    else:
        print("\nInvalid choice. Please try again.")
        fight_or_flee()

def battle_with_dragon():
    print("\nYou face the mighty dragon in a battle for your life!")
    print("Choose your actions wisely.")
    time.sleep(2)
    player_health = 100
    dragon_health = 100
    while player_health > 0 and dragon_health > 0:
        print("\nYour health:", player_health)
        print("Dragon's health:", dragon_health)
        action = input("Enter 'attack', 'defend', or 'heal': ").lower()
        if action == "attack":
            player_damage = random.randint(10, 20)
            dragon_damage = random.randint(10, 20)
            print("\nYou attack the dragon, dealing", player_damage, "damage!")
            print("The dragon retaliates, dealing", dragon_damage, "damage!")
            player_health -= dragon_damage
            dragon_health -= player_damage
        elif action == "defend":
            dragon_damage = random.randint(5, 10)
            print("\nYou defend against the dragon's attack, taking reduced damage.")
            print("The dragon attacks, dealing", dragon_damage, "damage!")
            player_health -= dragon_damage
        elif action == "heal":
            player_health += random.randint(10, 20)
            print("\nYou drink a healing potion and restore some health.")
            print("The dragon takes the opportunity to attack, dealing", dragon_damage, "damage!")
            player_health -= dragon_damage
        else:
            print("\nInvalid action. Choose 'attack', 'defend', or 'heal'.")
    if player_health <= 0:
        print("\nYou have been defeated by the dragon. Game over.")
        time.sleep(2)
        game_over()
    elif dragon_health <= 0:
        print("\nCongratulations, you have defeated the dragon!")
        print("You emerge victorious and continue on your quest.")
        time.sleep(2)
        dark_forest()

def game_over():
    print("\nGame over.")
    print("Thank you for playing!")

# Main function to start the game
def main():
    intro()
    forest_path()

# Run the game
if __name__ == "__main__":
    main()
