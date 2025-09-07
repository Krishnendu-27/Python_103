'''
Python Program to Check Prime Number
Python Program to Print all Prime Numbers in an Interval
Python Program to Find the Factorial of a Number
Python Program to Print the Fibonacci sequence
Python Program to Check Armstrong Number
Python Program to Find Armstrong Number in an Interval
Python Program to Find the Sum of Natural Numbers
Python Program to Find HCF or GCD
Python Program to Find LCM
Python Program to Find the Factors of a Number
Python Program to Make a Simple Calculator
'''
import math;
# Python Program to Check Prime Number

def isprime(num):
    if num <= 1:
        return f"{num} is not a prime number"
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime number"
    
    return f"{num} is a prime number"

    
print(isprime(9))

# Python Program to Print all Prime Numbers in an Interval

def is_isprime_range(num1, num2):
    if num1 <= 1:
        num1 = 2  # Start from 2 since primes are >= 2

    for i in range(num1, num2):
        is_prime = True  # Assume i is prime

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break  # No need to check further

        if is_prime:
            print(f"{i} is a prime number")

is_isprime_range(2, 20)

# Python Program to Find the Factorial of a Number

def fibo(num1):
    fibonachi = 1;
    for i in range (1,num1+1):
        fibonachi = fibonachi * i;
    return fibonachi;

print(fibo(5))

# Python Program to Find the Factorial of a Number
def fact(num):
    for i in range(1,num+1):
        for j in range (1,num+1):
            if i * j == num:
                print(i);

print(fact(10))

# Python Program to Check Armstrong Number

def armstrong (num):
    temp = num
    s = 0;
    for i in range (1,temp):
        r = temp % 10;
        s = s + (r ** 3)
        temp = temp // 10;

    if s == num :
        return (f"{num} is a amonstrong number")
    else:
        return (f"{num} is a NOT amonstrong number")
print(armstrong(153))

# Python Program to Find Armstrong Number in an Interval

def armstrong_intervel (start, end):
    for num in range(start, end + 1):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        if sum == num:
            print(num)
print(armstrong_intervel(100,500))