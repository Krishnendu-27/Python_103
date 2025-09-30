# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

# formulla: SI = (P × R × T) / 100

p = int(input("enter (Principal): "))
r = int(input("enter (rate): "))
t = int(input("enter (Time): "))

interest = (p*r*t) / 100;
print(interest)