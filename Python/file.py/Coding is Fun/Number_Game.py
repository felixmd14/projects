print('WELCOME to the NUMBER GUESSING GAME')
import random
correct_num = random.randint(1, 15)
num_entered = int(input('Guess a number between 1-15: '))
if num_entered < 1 or int(num_entered) > 15:
    Output = 'Your guess is not within the given limit, try again.'
elif num_entered < correct_num or num_entered > correct_num:
    Output = 'Wrong guess, try again.'
else:
    Output = f'You got the right answer; the answer is {correct_num}.'
print(Output)