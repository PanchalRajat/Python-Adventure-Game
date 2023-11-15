import time
import random

hero_health = 10
enemy_health = 10
hero_coins = 0


def engage_in_battle():
    global hero_health, enemy_health, hero_coins
    while True:
        action = input("Do you want to [p]unch, [k]ick, or [r]un away? ")
        if action == "p":
            damage = random.randint(1, 3)
            enemy_health -= damage
            print(f"You attacked the enemy and inflicted {damage} damage!")
        elif action == "k":
            damage = random.randint(2, 4)
            enemy_health -= damage
            print(f"You kicked the enemy and caused {damage} damage!")
        elif action == "r":
            print("You managed to escape from the enemy. Coward!")
            break
        else:
            hero_health -= 2
            print("You didn't make a move and got hit by the enemy!")
            if hero_health <= 0:
                print("You have been defeated!")
                break
            continue

        print(f'Hero Health: {hero_health}\nEnemy Health: {enemy_health}')

        if enemy_health <= 0:
            print("You have defeated the enemy!")
            hero_coins += 1
            break

        hero_health -= random.randint(1, 3)
        print("The enemy attacked you!")

        if hero_health <= 0:
            print("You have been defeated!")
            break


def embark_on_adventure():
    global hero_health, enemy_health, hero_coins
    print(
        "You find yourself at a path split. Do you want to go [l]eft towards the dark cave, [r]ight towards the bright side and river crossing, or [f]orward to the mysterious forest?")
    direction = input("Enter 'l', 'r', or 'f': ")

    if direction == "l":
        print("You entered the dark cave.")
        print("Do you want to explore the [d]eep part or the [s]hallow part?")
        sub_direction = input("Enter 'd' or 's': ")

        if sub_direction == "d":
            print("You ventured into the deep part of the cave and found a hidden treasure!")
            hero_coins += 5
        elif sub_direction == "s":
            print("You explored the shallow part of the cave but found nothing of interest.")
        else:
            print("Invalid input. Try again.")
            embark_on_adventure()
            return

    elif direction == "r":
        print("You reached the river crossing.")
        print("Do you want to [s]wim across or [b]uild a bridge?")
        sub_direction = input("Enter 's' or 'b': ")

        if sub_direction == "s":
            print("You bravely swam across the river and reached the other side.")
        elif sub_direction == "b":
            print("You decided to build a bridge and successfully crossed the river.")
        else:
            print("Invalid input. Try again.")
            embark_on_adventure()
            return

    elif direction == "f":
        print("You entered the mysterious forest and discovered a hidden path.")
        print("Do you want to [c]ontinue deeper into the forest or [b]acktrack towards the main path?")
        sub_direction = input("Enter 'c' or 'b': ")

        if sub_direction == "c":
            print("As you venture deeper, you encounter a mystical creature!")
            enemy_health = 15
        elif sub_direction == "b":
            print("You backtrack to the main path.")
            embark_on_adventure()
            return
        else:
            print("Invalid input. Try again.")
            embark_on_adventure()
            return

    else:
        print("Invalid input. Try again.")
        embark_on_adventure()
        return

    print("Do you want to [f]ight the enemy or [g]ive up?")
    action = input("Enter 'f' or 'g': ")

    if action == "f":
        print("You entered into a fight with the enemy!")
        engage_in_battle()
    elif action == "g":
        print("You gave up and lost the game!")
    else:
        print("Invalid input. Try again.")
        embark_on_adventure()
        return

    print(f"You have {hero_coins} coins in your inventory.")
    play_again = input("Do you want to play again? (y/n): ")

    if play_again.lower() == "y":
        hero_health = 10
        embark_on_adventure()
    else:
        print("Thanks for playing!")

embark_on_adventure()

