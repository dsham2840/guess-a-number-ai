#Guess A Number- AI Version
#
#Dylan Sham
#9/9/2016

import math
import random

def input_num():
    while True:
        num = input()

        if num.isnumeric():
            return int(num)
        else:
            print("That isn't a number, " + name + ". You know better.")
        
def starting_screen():
    print(" ____                                       ______      __  __                      __                              ")
    print("/\  _`\                                    /\  _  \    /\ \/\ \                    /\ \                             ")
    print("\ \ \ \_\  __  __     __    ____    ____   \ \ \_\ \   \ \ `\\ \  __  __    ___ ___\ \ \____     __   _ __    __    ")
    print(" \ \ \ _  /\ \/\ \  /'__`\ /',__\  /',__\   \ \  __ \   \ \ , ` \/\ \/\ \ /' __` __`\ \ '__`\  /'__`\/\`'__\ /\_\   ")
    print("  \ \ \/, \ \ \_\ \/\  __//\__, `\/\__, `\   \ \ \/\ \   \ \ \`\ \ \ \_\ \/\ \/\ \/\ \ \ \ \ \/\  __/\ \ \/  \/_/_  ")
    print("   \ \____/\ \____/\ \____\/\____/\/\____/    \ \_\ \_\   \ \_\ \_\ \____/\ \_\ \_\ \_\ \_,__/\ \____\\ \_\    /\_\ ")
    print("    \/___/  \/___/  \/____/\/___/  \/___/      \/_/\/_/    \/_/\/_/\/___/  \/_/\/_/\/_/\/___/  \/____/ \/_/    \/_/ ")
    print()
    print("  ______      ______          __  __                                               ")
    print(" /\  _  \    /\__  _\        /\ \/\ \                       __                     ")
    print(" \ \ \_\ \   \/_/\ \/        \ \ \ \ \     __   _ __   ____/\_\    ___     ___     ")
    print("  \ \  __ \     \ \ \         \ \ \ \ \  /'__`\/\`'__\/',__\/\ \  / __`\ /' _ `\   ")
    print("   \ \ \/\ \  __ \_\ \__  __   \ \ \_/ \/\  __/\ \ \//\__, `\ \ \/\ \_\ \/\ \/\ \  ")
    print("    \ \_\ \_\/\_\/\_____\/\_\   \ `\___/\ \____\\ \_\\/\____/\ \_\ \____/\ \_\ \_\ ")
    print("     \/_/\/_/\/_/\/_____/\/_/    `\/__/  \/____/ \/_/ \/___/  \/_/\/___/  \/_/\/_/ ")
    print()
    print("          Press Enter to Start the Game!")
    input()
    
def play():

    print("Choose the low value for the game, " + name  + "!")
    low = input_num()
    print("Choose the high value for the game, " + name  + "!")
    high = input_num()

    limit = int(math.log(int(high) - int(low), 2)) + 1
    tries = 0

    print("Welcome To Guess A Number: AI Version, " + name + "! Please think of a number from " + str(low) + " to " + str(high) + " and I will guess it.")
    input()
    print("This will be easy! I can guess your number in " + str(limit) + " tries!")
    print()
    
    correct = False

    while correct == False:
        guess = (int(high) + int(low)) // 2
        print("Is the number " + str(guess) + ", " + name + "?")
        print("Enter 'yes', 'lower', or 'higher' ")
        ans = input()
        print()
        
        if ans.lower() == 'lower' or ans.lower() == "l":
            high = guess - 1
        elif ans.lower() == 'higher' or ans.lower() == "h":
            low = guess + 1
        elif ans.lower() == 'yes' or ans.lower() == "y":
            correct = True
        else:
            print("What? I don't understand what you just said, " + name + ".")
            tries = tries - 1

        tries += 1

        if tries >= limit: 
            print("It seems like you made a mistake somewhere, I should have already guessed the answer :(")
            play_again()


    if correct == True:
        print("I told you I would get it! It only took me " + str(tries) + " tries, " + name + "!")

def play_again():

    while True:
        answer = input("Would you like to play again, " + name + "? ")

        if answer.lower() == 'no' or answer.lower() == "n":
            return False
        elif answer.lower() == 'yes' or answer.lower() == "y":
            return True

        print("Huh? Just say yes or no.")

def end_credits():
    print("Thanks for playing my game, " + name + "! This game was created by Dylan Sham.")
    print("Please rate this game from 1-10 on how fun it was!")
    rating = input_num()
    
    if int(rating) <= 3:
        print("Yikes")

    elif int(rating) > 3 and int(rating) <= 7:
        print("Noice!")

    elif int(rating) > 7 and int(rating) <=10:
        print(" r a d i c a l ")
    elif int(rating) > 10 and int(rating) <=50:
        print(" c h i l l o u t f a m ")
    else:
        print(" o h m y , t o o m u c h r a t i n g ")
                
        
#game begins
starting_screen()
print("What is your name, player?")
name = input()

again = True

while again == True:
    print()
    play()
    again = play_again()
    print()

print("Game over")
end_credits()

            


    
