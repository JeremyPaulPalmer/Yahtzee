import global_var
import dice_mod

def view_dice():
    #for each value in dice_list, show the graphic
    for i in global_var.dice_list:
        dice_mod.dice(i)

    #print total of roll
    print('\nTotal: ', sum(global_var.dice_list))

    #for each value in dice list, append to associated list
    for i in global_var.dice_list:
        if i == 1:
            global_var.ones_list.append(i)
        elif i == 2:
            global_var.twos_list.append(i)
        elif i == 3:
            global_var.threes_list.append(i)
        elif i == 4:
            global_var.fours_list.append(i)
        elif i == 5:
            global_var.fives_list.append(i)
        else:
            global_var.sixes_list.append(i)
            
    #print list values
    print('\nOnes:    (', len(global_var.ones_list),  ')', sum(global_var.ones_list))
    print('Twos:    (', len(global_var.twos_list),  ')', sum(global_var.twos_list))
    print('Threes:  (', len(global_var.threes_list),')', sum(global_var.threes_list))
    print('Fours:   (', len(global_var.fours_list), ')', sum(global_var.fours_list))
    print('Fives:   (', len(global_var.fives_list), ')', sum(global_var.fives_list))
    print('Sixes:   (', len(global_var.sixes_list), ')', sum(global_var.sixes_list))