import math

def arm_s(n):
    r = 0

    for i in range(3):
            a = int(n / 10)
            r = r + (n % 10)**3
            n = a
    if r == k:
        print(r)

print('The armstrong numbers are :')
for k in range(100,1000,1):
    arm_s(k)
