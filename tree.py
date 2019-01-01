import math

def arm_s(n):
    r = 0

    for i in range(3):
            a = int(n / 10)
            r = r + (n % 10)**3
            n = a
    if r == number:
        print('this is an armstrong number ')
    else:
        print('not an armstrong number ')

number = int(input('enter the number'))
arm_s(number)