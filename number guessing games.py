from random import randint
lower_num, higher_num = 1,10
random_number: int = randint(lower_num, higher_num)
print(f"guess the number in the range from{lower_num} to {higher_num}")

while True:
    try:
        user_guess: int = int(input('guess:'))
    except ValueError as e:
        print('please enter a valid number')
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
         print('The number is higher')
    else:
        print('You guess it!')
        break