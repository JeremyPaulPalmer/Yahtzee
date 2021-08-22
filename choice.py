import upper_lower
import global_var
import dice_mod

def choice():
    answer = input('\n(s)core, (r)oll again, or (k)eep dice? (s/r/k) ')
    while (answer != 's'.lower().strip()) and (answer != 'r'.lower().strip()) and (answer != 'k'.lower().strip()):
        choice()
    else:
        if answer == 's'.lower().strip():
            upper_lower.upper_lower()
        elif answer == 'r'.lower().strip():
            return
        elif answer == 'k'.lower().strip():
            print("Which dice would you like to keep?")
            for i in global_var.dice_list:
                dice_mod.dice(i)
                keep = input(' (y/n) ')
                if keep == 'y'.lower().strip():
                    global_var.kept_dice_list.append(i)
            global_var.dice_list = global_var.kept_dice_list    