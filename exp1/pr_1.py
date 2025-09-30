# Write a program to print grade of a student.

#get the input from user

marks = float (input("Enter your marks (0-1000): "))

# check the grade based on da marks

if marks >= 90:
    grade='A'
elif marks>= 80:
    grade = 'B' 
elif marks >- 70:
    grade = 'C'
elif marks >= 60:
    grade ='D'
else:
    grade = 'F'
    
#print the grade

print("Your grade is: ")
    