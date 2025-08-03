#  Program to Add Two Numbers

# num1 = int(input("enter the first number"));
# num2 = int(input("enter the first number"));

# num3 = num1 + num2;

# print("the sum of two number",num1 , "&" , num2 ,"is", num3);

# Program to Find the Square Root

# num4 = int(input("enter the first number"));
# squareroot = num4 ** 0.5;

# print("the square root of " , num4 , " is " , squareroot);

# Program to Calculate the Area of a Triangle

# base = int(input("enter the base"));
# height= int(input("enter the height"));

# area = 0.5 * base * height;
# print("the area of traingele is" , area , "when base is ", base ,  "when height is ", height);

# Program to Swap Two Variables

num5 = int(input("enter the first number"));
num6 = int(input("enter the secoend number"));
print("before swaping the first num" , num5);
print("before swaping the seconed num" , num6);
num5 = num5 +num6;
num6 = num5 - num6;
num5 = num5 - num6;
print("after swaping the first num" , num5);
print("after swaping the first num" , num6);

#Program to Convert Kilometers to Miles

# num7 = int(input("enter the Kilometers"));

# miles = 0.621371 * num7;
# print("the Kilometers is" , num7 , "then miles is", miles);

# Program to Convert Celsius To Fahrenheit

# num8 = int(input("enter the Celsius temprature"));

# Fahrenheit = (num7*1.8) +32
# print("the Fahrenheit is" , Fahrenheit , "when Celsius is" , num8);

# Program to Check if a Number is Odd or Even 

# num9 = int(input("enter the number"));
# if num9 % 2 == 0:
#     print(num9 , "is a Even number")
# else :
#     print(num9 , "is a Odd number")

# Program to Check if a Number is Positive, Negative or 0

# num10 = int(input("enter the number"));

# if num10 <= 0 :
#     print(num10 , "is a negative number")
# else:
#     print(num10 , "is a posetive number")

# Program to Check Leap Year

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Program to Find the Largest Among Three Numbers

num11 =  int(input("Enter the first number: "))
num12 =  int(input("Enter the secoend number: "))
num13 =  int(input("Enter the third number: "))

largest_num = max(num11 , num12 , num13)
print("the largest number between", num11 , num12 , num13 , "is" , largest_num)