import time
import sys
import random


# Gives players a description of what's happening.
def intro(creature):
    typing("You find yourself standing in an open field,"
           " filled with grass and yellow wildflowers.\n")
    typing("Rumor has it that a " + creature + " is somewhere around here,"
           " and has been terrifying the nearby village.\n")
    typing("In front of you is a house.\n")
    typing("To your right is a dark cave.\n")
    typing("In your hand you hold your trusty"
           " (but not very effective) dagger.\n\n")


# This function for delaying the text appearance on the screen with 2 seconds.
def pause(text):
    print(text)
    sys.stdout.flush()  # Without this line time.sleep() doesn't work in win10
    time.sleep(1)  # or just on my computer.


# This function for imitating typing
def typing(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


# Players can interact with the game.They have to pick an option (1 or 2).
def start_the_game(item, creature):
    pause("Enter 1 to knock on the door of the house.")
    pause("Enter 2 to peer into the cave.")

    answer = input("What would you like to do?\n(Please enter 1 or 2.)\n")
    while answer != '1' and answer != '2':
        answer = input("(Please enter 1 or 2.)\n")

    if answer == "1":
        house(item, creature)
    if answer == "2":
        cave(item, creature)


# This function is active when players choose the second option (into the cave)
def cave(item, creature):
    if "sword" in item:
        typing("You peer cautiously into the cave.\n")
        typing("You've been here before, and gotten all the good stuff."
               " It's just an empty cave now.\n")
        typing("You walk back out to the field.\n\n")
        start_the_game(item, creature)
    else:
        typing("You peer cautiously into the cave.\n")
        typing("It turns out to be only a very small cave.\n")
        typing("Your eye catches a glint of metal behind a rock.\n")
        typing("You have found the magical Sword of Ogoroth!\n")
        typing("You discard your silly old dagger and"
               " take the sword with you.\n")
        typing("You walk back out to the field.\n\n")
        item.append("sword")
        start_the_game(item, creature)


# This function is active when players choose the first option (knock on door).
def house(item, creature):
    yesno = "sword" in item
    typing("You approach the door of the house.\n")
    typing("You are about to knock when the door opens"
           " and out steps a " + creature + ".\n")
    typing("Eep! This is the " + creature + "'s house!\n")
    typing("The " + creature + " attacks you!\n")

    if not yesno:
        typing("You feel a bit under-prepared for this,"
               " what with only having a tiny dagger.\n")

    answer = input("Would you like to (1) fight or (2) run away?")
    while answer != '1' and answer != '2':
        answer = input("(Please enter 1 or 2.)\n")

    if answer == '1' and yesno:
        typing("As the " + creature + " moves to attack,"
               " you unsheath your new sword.\n")
        typing("The Sword of Ogoroth shines brightly in your hand as you "
               "brace yourself for the attack.\n")
        typing("But the " + creature + " takes one look at your"
               " shiny new toy and runs away!\n")
        typing("You have rid the town of the " + creature +
               ". You are victorious!\n")
        play_again()
    if answer == '1' and not yesno:
        typing("You do your best...\n")
        typing("but your dagger is no match for the " + creature + ".\n")
        typing("You have been defeated!\n")
        play_again()
    if answer == '2':
        typing("You run back into the field. Luckily,"
               " you don't seem to have been followed.\n\n")
        start_the_game(item, creature)


# This function allows players to finish the game or to restart it.
def play_again():
    play = input("Would you like to play again? (y/n)")
    if play == "y":
        print("Excellent! Restarting the game ...\n")
        prepare_to_start()
    elif play == "n":
        print("Thanks for playing! See you next time.")
    else:
        print("Wrong letter (y/n)! Try it again!")
        play_again()


# This function sets the initial values.
def prepare_to_start():
    items = ["dagger"]
    creatures = ["pirate", "griffin", "deathclaw", "giant ogre",
                 "dragon", "huge rat", "mouse"]
    creature = random.choice(creatures)  # Randomly choose a creature
    intro(creature)
    start_the_game(items, creature)


prepare_to_start()
