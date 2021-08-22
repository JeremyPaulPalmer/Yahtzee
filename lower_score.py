import global_var
import upper_lower
import card
import time

#Checks dice_hist list for 3 of one kind
def three_kind(list):
    for dice in list:
        if dice >= 3:
            return True
    return False

#Checks dice_hist list for 4 of one kind
def four_kind(list):
    for dice in list:
        if dice >= 4:
            return True
    return False

#Checks dice_hist list for 3 of one and 2 of one
def full_house(list):
    two = False
    three = False
    for i in list:
        if i == 3:
            three = True
        if i == 2:
            two = True
        if two and three:
            return True
    return False

#Checks 3 scenarios for small straight
def sm_str(list):
    counter = 0
    for i in range(0, 4):
        if list[i] > 0:
            counter += 1
            print(counter)
        if counter == 4:
            return True
    counter = 0
    for i in range(1, 5):
        if list[i] > 0:
            counter += 1
        if counter == 4:
            return True
    counter = 0
    for i in range(2, 6):
        if list[i] > 0:
            counter += 1
        if counter == 4:
            return True
    return False

#Checks 2 scenarios for large straight
def lg_str(list):
    counter = 0
    for i in range(0, 5):
        if list[i] > 0:
            counter += 1
        if counter == 5:
            return True
    counter = 0
    for i in range(1, 6):
        if list[i] > 0:
            counter += 1
        if counter == 5:
            return True
    return False
            

def lower_score():   

    global_var.dice_hist.append(len(global_var.ones_list))
    global_var.dice_hist.append(len(global_var.twos_list))
    global_var.dice_hist.append(len(global_var.threes_list))
    global_var.dice_hist.append(len(global_var.fours_list))
    global_var.dice_hist.append(len(global_var.fives_list))
    global_var.dice_hist.append(len(global_var.sixes_list))

    score = (input('Where would you like to score? (1-7) '))
    while score != '1' and score != '2' and score != '3' and score != '4' and score != '5' and score != '6' and score != '7': 
        score = (input('Where would you like to score? (1-7) '))
    if score == '0' or score >= '8':
        score = ''
        lower_score()
    while score:
        if score == 'one'.lower().strip() or score == '1':
            if isinstance(global_var.threek, int):
                print('Already scored. Try again!')
                upper_lower.upper_lower()
            elif global_var.threek == '__' and three_kind(global_var.dice_hist):
                global_var.threek = sum(global_var.dice_list)
                global_var.lower_sub_list.append(global_var.threek)
                global_var.counter_lower += 1
                score = ''
            else:
                global_var.threek = 0
                global_var.counter_lower += 1
                score = ''
        elif score == 'two'.lower().strip() or score == '2':
            if isinstance(global_var.fourk, int):
                print('Already scored. Try again!')
                upper_lower.upper_lower()
            elif global_var.fourk == '__' and four_kind(global_var.dice_hist):
                global_var.fourk = sum(global_var.dice_list)
                global_var.lower_sub_list.append(global_var.fourk)
                global_var.counter_lower += 1
                score = ''
            else:
                global_var.fourk = 0
                global_var.counter_lower += 1
                score = ''
        elif score == 'three'.lower().strip() or score == '3':
            if isinstance(global_var.house, int):
                print('Already scored. Try again!')
                upper_lower.upper_lower()
            elif global_var.house == '__' and full_house(global_var.dice_hist):
                global_var.house = 25
                global_var.lower_sub_list.append(global_var.house)
                global_var.counter_lower += 1
                score = ''
            else:
                global_var.house = 0
                global_var.counter_lower += 1
                score = ''
        elif score == 'four'.lower().strip() or score == '4':
            if isinstance(global_var.sm_str, int):
                print('Already scored. Try again!')
                upper_lower.upper_lower()
            elif global_var.sm_str == '__' and sm_str(global_var.dice_hist):
                global_var.sm_str = 30
                global_var.lower_sub_list.append(global_var.sm_str)
                global_var.counter_lower += 1
                score = ''
            else:
                global_var.sm_str = 0
                global_var.counter_lower += 1
                score = ''
        elif score == 'five'.lower().strip() or score == '5':
            if isinstance(global_var.lg_str, int):
                print('Already scored. Try again!')
                upper_lower.upper_lower()
            elif global_var.lg_str == '__' and lg_str(global_var.dice_hist):
                global_var.lg_str = 40
                global_var.lower_sub_list.append(global_var.lg_str)
                global_var.counter_lower += 1
                score = ''
            else:
                global_var.lg_str = 0
                global_var.counter_lower += 1
                score = '' 
        elif score == 'six'.lower().strip() or score == '6':
            if isinstance(global_var.yahtzee, str):
                global_var.yahtzee = 0
                global_var.lower_sub_list.append(global_var.yahtzee)
                global_var.counter_lower += 1
                score = ''
            elif global_var.yahtzee == 0:
                print('Already scored. Try again!')
            else:
                global_var.yaht_bon_list.append(100)
                global_var.yaht_bon = sum(global_var.yaht_bon_list)
        elif score == 'seven'.lower().strip() or score == '7':
            if isinstance(global_var.chance, int):
                print('Already scored. Try again!')
                upper_lower.upper_lower()
            elif global_var.chance == '__':
                global_var.chance = sum(global_var.dice_list)
                global_var.lower_sub_list.append(global_var.chance)
                global_var.counter_lower += 1
                score = ''
            else:
                global_var.chance = 0
                global_var.counter_lower += 1
                score = ''
    
        card.card()
        time.sleep(2)
        global_var.roll_counter = 0
        global_var.dice_list = []
        global_var.dice_hist = []