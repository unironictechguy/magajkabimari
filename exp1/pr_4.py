#d) Write a program to make sum of first n numbers using while loop.
num = int(input("Enter da numbers u want sum of: "))

count = 1
sum = 0

while count <= num:
    sum += count
    count+=1
    
print("Your sum is:", sum)