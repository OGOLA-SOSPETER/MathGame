"""
This is a game for children
"""
from random import randint
import random

num1 = randint(1,10)
num2 = randint(1,10)
prod1 = num1*num2
p = 0
win = 0
operator = ['x','+','/','-']

print('How many attempts do you want to make?')
counter = eval(input())
new_counter = counter - 1
for p in range(counter):
    num1 = randint(10,100)
    num2 = randint(1,120)
    result = 1
    operator_select = random.choice(operator)
    if operator_select == 'x':
        result = num1*num2

    elif operator_select == '+':
        result = num1 + num2

    elif operator_select == '/':
        result = num1/num2

    elif operator_select == '-':
        result = num1 - num2

    print('\nQuestion', p+1,' : ',num1, operator_select, num2, ' =  _____?')
    answer = eval(input('Answer = : '))
    #prod1
    if answer == result:
        win += 1
        print('Congratulations!! \n You are a wit...')

    else:
        print('You cannot disapprove the checker!!!!! \n The correct answer = ', result)

print('\nYou scored a total of {:3d}  Out of the possible {:3d} '.format(win,counter))
print('This represents a percentage score of {:.2f} %'.format((win/new_counter)*100))
