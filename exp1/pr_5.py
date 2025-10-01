# Write a program to print 10 random numbers between 1 to 100 using for loop

# import random module

import random

# to run loop 10 times
for i in range(10):
    
    num = random.randint(1,100)
    print(num)