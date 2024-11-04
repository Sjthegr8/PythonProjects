################################################################################
#
# Computer Project 02
#
# Description:
#       This python script is designed to play a mathematical game where two players take turns
#       removing stones from two distinct piles. There are two players in this game which includes you and
#       the computer. Both of the users go head to head by the following steps:
#
#       1. Prompts the user to input if they like to play or not
#       2. prompts the user to input the number of stones they need to put in both the piles
#       3. The user starts the game by removing stones from a pile
#       4. Then the computer takes the turn and this goes on
#       5. The game is put to an end when both the piles have none stones
#       6. The score is also calculated and user has the option to play again
#
################################################################################


# DO NOT MODIFY THE FOLLOWING 2 LINES OR YOU RISK TO NOT PASS THE TESTS
import random
random.seed(10)

# USE THE FOLLOWING IN YOUR PRINT AND INPUT STATEMENTS
":~Would you like to play? (0=no, 1=yes) ~:"
":~How many stones per pile would you like to play? ~:"
"Start --> Pile 1:"
"   Pile 2:"
"\nStarting a new game..."
"Pile must be 1 or 2 and non-empty. Please try again."
"Invalid number of stones. Please try again."
":~Choose a pile (1 or 2) ~:"
":~Choose stones to remove from pile ~:"
#"Player -> ",end=''
#"Computer -> ",end=''
"Pile 1:"
"   Pile 2:"
"\nComputer wins!"
"\nCONGRATULATIONS! Player wins!"
"You actually won! Did you cheat?"
"Enjoy your bragging rights (for now). I am coming back stronger!"

"\nThanks for playing! See you again soon!"
"Score -> human:"
"; computer:"
"Remove"
"stones from pile"



#Display the rules of the game
banner = """*** Welcome to the Game of Nim! ***
*Spoiler Alert: I am probably going to win...* 
"""

rules="""Nim is a deceptively simple two-player game where stones mysteriously disappear,
one, two, or three at a time!
The game kicks off with two piles of stones, cleverly named Pile 1 and Pile 2 
(because creativity matters!). Players take turns. 
On your turn, pick a pile and decide how many stones to make vanish: 1, 2, or 3.
The goal? Be the one to remove the very last stone and victory!
But hey, do not feel bad when you lose...I have had lots of practice!"""

print(banner)
print(rules)
print( )
agree = int(input(":~Would you like to play? (0=no, 1=yes) ~:"))
score_human=0
score_computer=0

while True:

    if agree == 0:
        "\nThanks for playing! See you again soon!"
        break

    if agree == 1:
        print("\nStarting a new game...")
        stone = stone_one = stone_two =int(input(":~How many stones per pile would you like to play? ~:"))
        print("Start --> Pile 1:", stone_one, "   Pile 2:", stone_two)

    while True:
        if stone>0:
            pile = int(input(":~Choose a pile (1 or 2) ~:"))
            if pile == 1:
                if stone_one == 0 and stone_two != 0:
                    print("Pile must be 1 or 2 and non-empty. Please try again.")
                    continue

                while True:
                    a = int(input(":~Choose stones to remove from pile ~:"))
                    if a > 3:
                        print("Invalid number of stones. Please try again.")

                    else:
                        break
                while True:

                    if a <= stone_one :
                        break
                    print("Invalid number of stones. Please try again.")
                    a = int(input(":~Choose stones to remove from pile ~:"))
                stone_one -= a
                print("Player -> Remove", a, "stones from pile", pile)
                print("Pile 1:",stone_one,"   Pile 2:",stone_two)

                if stone_one == 0 and stone_two==0:
                    print("\nCONGRATULATIONS! Player wins!")
                    print("You actually won! Did you cheat?")
                    print("Enjoy your bragging rights (for now). I am coming back stronger!")
                    score_human+=1
                    print("Score -> human:",score_human,"; computer:",score_computer)
                    agree_one = int(input(":~Would you like to play again? (0=no, 1=yes) ~:"))
                    if agree_one == 0:
                        print("\nThanks for playing! See you again soon!")
                        exit()

                    if agree_one == 1:
                        break
            elif pile == 2:
                if stone_two == 0 and stone_one != 0:
                    print("Pile must be 1 or 2 and non-empty. Please try again.")
                    continue
                while True:
                    b = int(input(":~Choose stones to remove from pile ~:"))
                    if b > 3:
                        print("Invalid number of stones. Please try again.")
                    else:
                        break

                while True:
                    if b <= stone_two:
                        break
                    print("Invalid number of stones. Please try again.")
                    b = int(input(":~Choose stones to remove from pile ~:"))
                stone_two -= b
                print("Player -> Remove", b,"stones from pile", pile)
                print("Pile 1:",stone_one,"   Pile 2:",stone_two)

                if  stone_two == 0 and stone_one == 0:
                    print("\nCONGRATULATIONS! Player wins!")
                    print("You actually won! Did you cheat?")
                    print("Enjoy your bragging rights (for now). I am coming back stronger!")
                    score_human += 1
                    print("Score -> human:",score_human,"; computer:",score_computer)
                    agree_one = int(input(":~Would you like to play again? (0=no, 1=yes) ~:"))
                    if agree_one == 0:
                        print("\nThanks for playing! See you again soon!")
                        exit()
                    if agree_one == 1:
                        break
            if pile != 1 and pile != 2:
                print("Pile must be 1 or 2 and non-empty. Please try again.")
                continue

            if pile == 1 and stone_two != 0:
                comp_st = random.randint(1, 3)
                if comp_st > stone_two:
                    comp_st = stone_two
                stone_two = stone_two - comp_st
                print("Computer -> Remove",comp_st,"stones from pile 2")

            elif pile == 2 and stone_one != 0:
                comp_st = random.randint(1, 3)
                if comp_st > stone_one:
                    comp_st = stone_one
                stone_one = stone_one - comp_st
                print("Computer -> Remove",comp_st,"stones from pile 1")

            elif pile == 1 and stone_two == 0:
                comp_st = random.randint(1, 3)
                if comp_st > stone_one:
                    comp_st = stone_one
                stone_one = stone_one - comp_st
                print("Computer -> Remove",comp_st,"stones from pile 1")

            elif pile == 2 and stone_one == 0:
                comp_st = random.randint(1, 3)
                if comp_st > stone_two:
                    comp_st = stone_two
                stone_two = stone_two - comp_st
                print("Computer -> Remove",comp_st,"stones from pile 2")

            print("Pile 1:",stone_one,"   Pile 2:",stone_two)

            if stone_one == 0 and stone_two == 0:

                score_computer = score_computer + 1
                print("")
                print("Computer wins!")
                print("Score -> human:",score_human,"; computer:",score_computer)
                agree_one = int(input(":~Would you like to play again? (0=no, 1=yes) ~:"))
                if agree_one == 0:
                    print("\nThanks for playing! See you again soon!")
                    exit()

                if agree_one == 1:
                    break
                break
    else:
        print("Invalid number of stones. Please try again.")

if agree == 0:
    print("\n Thanks for playing! See you again soon!")
