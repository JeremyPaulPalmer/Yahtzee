import upper_score
import lower_score
import card
import global_var

def upper_lower():
    card.card()
    if global_var.counter_lower == 7:
        upper_score.upper_score()
    if global_var.counter_upper == 6:
        lower_score.lower_score()
    answer = input('\nWhere would you like to score? Upper or Lower? (u/l) ')
    while (answer != 'u'.lower().strip()) and (answer != 'l'.lower().strip()):
        answer = input('Please enter Upper or Lower (u/l) ')
    else:
        if answer == 'u'.lower().strip():
            upper_score.upper_score()
        else:
            lower_score.lower_score()