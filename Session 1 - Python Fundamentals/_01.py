# python Output
# print is a function 
print("its is a case sensetive langauge");
# mens A and a are diffrent

# we use invited comma for string in python
print("halo " , 1 , 5.5 , True)
# we use separeter in print for gieving diffren types of input

print("halo " , 1 , 5.5 , True , sep="/")

#2. data types

# interger
# it store 1*10^308 max
print(1e308) 
# decimal / float
# it store 1.7*^308 max 
print(1.7e308);
# boolean
print(True)
print(False)
#string
print("tere ma ki pranam ")
# complex
print(5+6j);
# list or array
print([1,3,4,5])
# tuple simmiler to list but have diffrent work
print((1,2,3,4,5))
# sets
print({1,2,3,4,5})
# dictionary
print({'name' : "krish" , 'gender' : "male" , 'age' : 5+6j })

# type : help us to chek what data type presnt

print(type(5.6))

#3. variables 

# python variables is dynamic
# so it doesnot need type for declaration of variable
num = 50;
print(num)
# we can store multiple type of value so its  dynamic binding. mense in a variable it can store string interger , float anything 
# its not like the static typing 
num = True;
print(num)
# we can store value like this . stylise way to write
a, b,c = 1,2,3;
print(a , b , c)
# we can store value like this for write same value
a=b=c = 5;
print(a , b , c)

# 4. keywords & identifers 
# conversation: its a process to convert high level programing language to binary language

# in python there 32 keyword

# keyword mens : it resevrr word for python. keyword not allow to write it as variable name

# identifier / variable name  

# 6. user input
# for input in python we use 
# input ()
input("enter tera name: ");

# input  2 number then return the sum
# here we do type convertion so its convert in int 
# when we took input its store in string beause it is a universal data format
num1 = int(input("num  1 : "))
num2 = int(input("num  1 : "))
num3 = num1 + num2
# here we learn after type convertion it wont change in orginal data it creat a new value and we worked on that new value that is convert
# explicit: when python covert type by himself 
# implicit: when we do manualy convert type by ourself
a = '5';
print(type(a))
b = int(a)
print(type(a))
print(type(b))
int(a)
print(type(a))
print(num3)

# 7. litleralas / value

# the value of variable is called litleralas
# interger literals
decimal_num = 10
binary_literal = 0b1010
octal_literal = 0o12
hex_literal = 0xA

print(f"Decimal: {decimal_num}")
print(f"Binary literal: {binary_literal}")
print(f"Octal literal: {octal_literal}")
print(f"Hexadecimal literal: {hex_literal}")

# float literal

float_1 = 10.5;
float_2 = 1.5e3; # 1.5 * 10^3
float_3 = 1.5e-3; # 1.5 * 100 10^-3

print(float_1)
print(float_2)
print(float_3)

# coplex number 
x = 3.14+9j;
print(x , x.imag , x.real)

# string
# when we use multiline string with more than one line we use """ """ string

# Different string literals
a = 'Hello'      # Single-quoted
b = "Python"     # Double-quoted
c = '''This is 
a multi-line string'''  # Triple-quoted
d = r"C:\Users\Python"  # Raw string
copyright_symbol = "\u00A9"  # Unicode code point for the copyright symbol
raw_str = r"raw \n bro";
print(a)
print(b)
print(c)
print(d)
print(copyright_symbol)
print(raw_str)

a = True + 4;
b = False + 4;
print(a) # ans will be 5 beacuse True = 1
print(b) # ans will be 4 beacuse False = 0

z = None # its men nothing
print(z)
# we can not delcare a variable before we use like otehr langauge so we use None for garbage value like others lanaguage