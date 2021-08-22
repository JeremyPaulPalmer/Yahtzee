import global_var
import time
import card

def upper_score():

    score = (input('Where would you like to score? (1-6) '))
    while score != '1' and score != '2' and score != '3' and score != '4' and score != '5' and score != '6': 
        score = (input('Where would you like to score? (1-6) '))
    if score == '0' or score >= '7':
        score = ''
        upper_score()
    while score:
            if score == 'ones'.lower().strip() or score == '1':
                if global_var.ones == '__':
                    global_var.ones = sum(global_var.ones_list)
                    global_var.upper_sub_list.append(global_var.ones)
                    global_var.subtotal = sum(global_var.upper_sub_list)
                    global_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'twos'.lower().strip() or score == '2':
                if global_var.twos == '__':
                    global_var.twos = sum(global_var.twos_list)
                    global_var.upper_sub_list.append(global_var.twos)
                    global_var.subtotal = sum(global_var.upper_sub_list)
                    global_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'threes'.lower().strip() or score == '3':
                if global_var.threes == '__':
                    global_var.threes = sum(global_var.threes_list)
                    global_var.upper_sub_list.append(global_var.threes)
                    global_var.subtotal = sum(global_var.upper_sub_list)
                    global_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'fours'.lower().strip() or score == '4':
                if global_var.fours == '__':
                    global_var.fours = sum(global_var.fours_list)
                    global_var.upper_sub_list.append(global_var.fours)
                    global_var.subtotal = sum(global_var.upper_sub_list)
                    global_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'fives'.lower().strip() or score == '5':
                if global_var.fives == '__':
                    global_var.fives = sum(global_var.fives_list)
                    global_var.upper_sub_list.append(global_var.fives)
                    global_var.subtotal = sum(global_var.upper_sub_list)
                    global_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')
            if score == 'sixes'.lower().strip() or score == '6':
                if global_var.sixes == '__':
                    global_var.sixes = sum(global_var.sixes_list)
                    global_var.upper_sub_list.append(global_var.sixes)
                    global_var.subtotal = sum(global_var.upper_sub_list)
                    global_var.counter_upper += 1
                    score = ''
                else:
                    print('Already scored. Try again!')
                    score = input('\nWhere would you like to score?\n')

            card.card()
            time.sleep(2)
            global_var.roll_counter = 0
            global_var.dice_list = []
            global_var.dice_hist = []