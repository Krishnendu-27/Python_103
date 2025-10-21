# Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
print("before num1 is " , num1 , "num2 is " , num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("after num1 is " , num1 , "num2 is " , num2)