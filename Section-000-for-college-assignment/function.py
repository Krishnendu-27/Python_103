# ============================================================
# FUNCTION PRACTICE PROBLEMS
# Solve each problem by writing Python code below the question.
# ============================================================


# ------------------------------------------------------------
# 1. DEFINING & CALLING FUNCTIONS
# ------------------------------------------------------------

# 1. Write a function that takes a number and prints whether it is even or odd.
# Code here:


def evenodd(num):
    if num % 2 == 0:
        print(f"{num} is a even")
    else:
        print(f"{num} is a odd")


evenodd(56)

# 2. Write a function that returns the square of a number.
# Code here:


def square(num):
    print(f"square of {num} is {num * num}")


square(50)
# ------------------------------------------------------------
# 2. RETURN VALUES
# ------------------------------------------------------------

# 3. Write a function that returns both area and circumference of a circle.
# Code here:


def both(r):
    area = 2 * 3.1415 * r
    circumference = 3.1415 * (r * r)

    print(f"area of {r} is  {area}")
    print(f"area of {r} is  {circumference}")


both(10)

# 4. Write a function that returns the largest of three numbers.
# Code here:


def largest(num1, num2, num3):
    maxx = max(num1, num2, num3)
    print(f"between {num1} {num2} {num3} is {maxx}")


largest(50, 80, 150)

# ---------------------- --------------------------------------
# 3. ARGUMENT TYPES
# ------------------------------------------------------------


# 5. Write a function with positional arguments to add three numbers.
# Code here:
def add_three_numbers(a, b, c):
    total = a + b + c
    return total


result = add_three_numbers(5, 10, 2)

print(f"The sum is: {result}")

# 6. Write a function with a default argument (country="India").
# Code here:


def country(c="India"):
    print(f"{c} is the best country")


country()

# 7. Write a function using keyword arguments (name, age).
# Code here:


def keyarg(name, age):
    print(f"Name is {name} and age is {age}")


keyarg("krish", 20)


# 8. Write a function that accepts variable-length arguments using *args.
# Code here:


# 9. Write a function that accepts **kwargs and prints key-value pairs.
# Code here:


# ------------------------------------------------------------
# 4. LOCAL & GLOBAL VARIABLES
# ------------------------------------------------------------

# 10. Write a program that demonstrates difference between local and global variables.
# Code here:


# ------------------------------------------------------------
# 5. RECURSIVE FUNCTIONS
# ------------------------------------------------------------

# 11. Write a recursive function to calculate factorial.
# Code here:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result1 = factorial(5)
print(result1)
# 12. Write a recursive function to print numbers from 1 to N.
# Code here:


def printnum(num):
    if num == 0:
        return 1
    else:
        print(num)
        printnum(num - 1)


printnum(10)

# ------------------------------------------------------------
# 6. LAMBDA FUNCTIONS
# ------------------------------------------------------------

# 13. Use filter() with lambda to print only even numbers from a list.
# Code here:


def get_even_numbers(numbers_list):
    # Create an empty list to store the even numbers we find
    even_list = []

    # Loop through every number in the input list
    for number in numbers_list:
        # Check if the number is even using the modulo operator (%)
        if number % 2 == 0:
            # If it is even, add it to our new list
            even_list.append(number)

    # Once the loop is finished, return the list of even numbers
    return even_list


my_list = [50, 60, 70, 80, 99, 109]
# Call the function with our data
result = get_even_numbers(my_list)

print(f"Original list: {my_list}")
print(f"Even numbers using a function: {result}")
# 14. Use map() with lambda to cube every number in a list.
# Code here:


# 15. Write a lambda function to find the largest of two numbers.
# Code here:


# ============================================================
# END OF FUNCTION EXERCISES FILE
# ============================================================
