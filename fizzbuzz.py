# Fizz Buzz playing code to learn pythin basics
# Created 14/08/2022

ii = 1
x = int(input("How high would you like to go?\n"))

while(ii <= x):
    if(ii % 15 == 0):
        print('Fizz Buzz')
    elif(ii % 3 == 0):
        print('Fizz')
    elif(ii % 5 == 0):
        print('Buzz')
    else:
        print(ii)
    ii += 1