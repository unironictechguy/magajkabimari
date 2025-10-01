#take da input 

num = int(input("Enter da number u want to find factorial for: "))

#initialize da factorial

factorial = 1

for i in range(1, num + 1):
    factorial*=i

print("Factorial of",num, "is", factorial)