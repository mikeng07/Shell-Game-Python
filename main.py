import random
import check_input


def main():
    money = 100
    play = True
    print("-Shell Game-")
    print("Find the Ball to double your bet")

    while play:

        #prompt bet and guess
        print()
        print("you have $" + str(money) + "." )
        bet = check_input.get_int_range("Bet amount? ", 1, money)
        print("  ___     ___     ___ ")
        print(" /   \   /   \   /   \ ")
        print("/  1  \ /  2  \ /  3  \ ")
        print("------- ------- ------- ")   
        ball_location = random.randint(1,3)
        user_guess = check_input.get_int_range("Make a guess: ", 1, 3)
        
        #display results
        print("  ___     ___     ___ ")
        print(" /   \   /   \   /   \ ")
        if (ball_location == 1):
            print("/  0  \ /     \ /     \ ")
        elif (ball_location == 2):
            print("/     \ /  0  \ /     \ ")
        else:
            print("/     \ /     \ /  0  \ ")

        print("------- ------- ------- ")  

        #check results
        if (ball_location == user_guess):
            print("Congratulations!")
            money = money + bet
        else:
            print("Sorry... you lose. ")
            money = money - bet

        #if if user have any money left 
        if(money <= 0):
            print("You're out of money!  Game over.")
            play = False 
        else:
            play = check_input.get_yes_no("Play again? (Y/N): ")
        

main()