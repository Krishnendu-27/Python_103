import math

# Python Program to Check Prime Number
def primecheker(x):
    isprime = 1
    for i in range(2,x/2):
        if(x%i== 0):
            isprime = 0
            break
        else:
            isprime = 1
    if(isprime == 1):
        print("its is a prime number")
    else:
        print("its is NOT a prime number")

# primecheker(10)

# Python Program to Print all Prime Numbers in an Interval
def primerange(start , end):
    isprime = 1;
    for i in range(start,end+1):
        for j in range(2 , i):
            if(i%j == 0):
                isprime = 0
                break;
            else:
                isprime = 1
        if(isprime == 1):
            print(f"{i} its is a prime number")

# primerange(2, 10);

# Python Program to Find the Factorial of a Number

def factorial(x):
    total = 1
    for i in range(1,x+1):
        total = total * i;
    print(f"factorial of {x} is {total}")

# factorial(5)

# Python Program to Print the Fibonacci sequence

def fibonacci(x):
    a = 0
    b = 1
    count = 0
    while(x > 0):
        print(a, end=" ")
        temp = a
        a = b
        b = temp + b
        # count += 1
        x = x-1

# fibonacci(10);

# Python Program to Check Armstrong Number

def armstrong(x):
    temp = x
    p = 0
    l = len(str(x))
    while(temp>0):
        r = temp % 10;
        p = r**l + p
        temp = temp // 10
    if(p == x):
        print(f"{x} is a Armstrong Number")   
    else:     
        print(f"{x} is not  a Armstrong Number")    

# armstrong(153)

# Python Program to Find Armstrong Number in an Interval

def armstrongintervel(start , end):
    for i in range(start , end):
        temp = i
        p = 0
        l = len(str(temp))
        while(temp>0):
            r = temp % 10;
            p = r**l + p
            temp = temp // 10
        if(p == i):
            print(f"{i} is a Armstrong Number")   

# armstrongintervel(100,500)

# Python Program to Find the Sum of Natural Numbers 
# formulla : sum = input * (input + 1) // 2

def naturalnum(x):
    sum = 0
    for i in range(1, x+1):
        sum = i * (i+1) // 2
    print(f"the Sum of Natural Number of {i} is {sum}")

naturalnum(10);

# Python Program to Find HCF or GCD

def hcf(a, b):
    result = math.gcd(a, b)
    print(f"HCF of {a} , {b} is {result}")
    return result  # ✅ return it so other functions can use it

hcf(10,20)

# Python Program to Find LCM

def lcm(x, y):
    return  x * y // hcf(x,y);
    # print(f"LCM of {x} , {y} is {ans2}")

print(f"LCM of 12 , 18 is {lcm(12,18)}")
