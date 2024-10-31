import random

correct_number = random.randrange(45)
attempts = 0
chances = 5

while attempts < chances:
    attempts += 1
    my_attempt = int(input('Please insert a number from 0 to 45: '))

    if my_attempt == correct_number:
        print(f'Congrats, the correct number if {correct_number}, you got it on your {attempts} time.')
        break
    
    elif attempts >= chances:
     
        print(f"You lost the correct number was {correct_number}")
    elif my_attempt > correct_number:
        print('Too big, try a smaller number')
    elif my_attempt < correct_number:
        print("Too small, try a different number")
    else:
        print('Not valid')