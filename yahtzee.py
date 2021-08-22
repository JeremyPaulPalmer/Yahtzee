import global_var
import dice_roll
import os
import sys
import view_dice
import upper_lower
import card
import choice
import time

print('Welcome to Yahtzee!')
card.card()


def play():

    print('Roll', global_var.roll_counter + 1)
    time.sleep(2)

    full_upper = False
    full_lower = False
    
    #while upper and lower not full, keep going
    while full_upper == False or full_lower == False:

        #initial roll
        if global_var.kept_dice_list == [] or global_var.kept_dice_list == 5:
            dice_roll.roll(5)
            global_var.roll_counter += 1
        else:
            dice_roll.roll(5 - len(global_var.kept_dice_list))
            for i in global_var.kept_dice_list:
                global_var.dice_list.append(i)
            global_var.roll_counter += 1
            global_var.kept_dice_list = []
        
        #view dice
        view_dice.view_dice()

        #prompt user to choose between score, roll again or keep dice
        if global_var.roll_counter < 3:
            choice.choice()
        else:
            upper_lower.upper_lower()
        
        #check to see if counters are 6 and 7 respectively in which case full equals True and the loop breaks.
        if global_var.counter_upper == 6:
            full_upper = True

        if global_var.counter_lower == 7:
            full_lower = True

        #reinitialize lists
        global_var.ones_list = []
        global_var.twos_list = []
        global_var.threes_list = []
        global_var.fours_list = []
        global_var.fives_list = []
        global_var.sixes_list = []
        global_var.dice_list = []
        global_var.dice_hist = []

        #check subtotal to see if the bonus is achieved
        if full_upper:
            if global_var.subtotal > 63:
                global_var.upper_bonus = 35
                global_var.total_upper = global_var.subtotal + global_var.upper_bonus
            else:
                global_var.upper_bonus = 0
                global_var.total_upper = global_var.subtotal

        if full_lower:
            global_var.total_lower = sum(global_var.lower_sub_list)

        if full_lower and full_upper:
            global_var.grand_total = global_var.total_lower + global_var.total_upper
            card.card()
            answer = input('Great game! Would you like to play again? (y/n) ')
            if answer == 'yes'.lower().strip() or answer == 'y'.lower().strip():
                os.execv(__file__, sys.argv)

    
    




if __name__ == "__main__":
    play()