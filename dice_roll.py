import random
import global_var
import upper_lower
import dice_mod

def roll(number): 
    #dice = []
    for i in range(1, number + 1):
        n = random.randint(1, 6)
        global_var.dice_list.append(n)