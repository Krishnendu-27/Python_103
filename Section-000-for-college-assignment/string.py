# ============================================================
# STRING PRACTICE PROBLEMS
# Solve each problem by writing Python code below the question.
# ============================================================


# ------------------------------------------------------------
# 1. BASIC TRAVERSING
# ------------------------------------------------------------

# 1. Write a program to print every character of a string on a new line.
# Code here:


s = "hallo bro"

for i in s:
    print(i)

# 2. Count how many vowels are present in a string.
# Code here:
vowels = "aeiou"
count = 0
for i in s:
    if i in vowels:
        count = count + 1
print(f"string have in '{s}' is {count}")

# ------------------------------------------------------------
# 2. CONCATENATION & REPLICATION
# ------------------------------------------------------------

# 3. Take two strings as input and concatenate them without using '+'.
# Code here:
s1 = "my name is "
s2 = "Krish "
s3 = "%s %s" % (s1, s2)
print(f"new string is {s3}")

# 4. Print a string 10 times using replication (* operator).
# Code here:

print(s2 * 10)

# ------------------------------------------------------------
# 3. MEMBERSHIP & COMPARISON
# ------------------------------------------------------------

# 5. Check if the substring "py" exists inside the given string.
# Code here:

s4 = "python is the great language"
print("py" in s4)

# 6. Compare two strings and print which one is lexicographically greater.
# Code here:

s5 = "appele"
s6 = "bananna"
if s5 > s6:
    print(f"in {s5} and {s6} lexicographically greater is {s5}")
else:
    print(f"in {s5} and {s6} lexicographically greater is {s6}")


# ------------------------------------------------------------
# 4. UNICODE
# ------------------------------------------------------------

# 7. Input a character and print its Unicode value using ord().
# Code here:

s7 = "a"
print(f"the character {s7} is {ord(s7)}")

# 8. Take a Unicode value and print the corresponding character using chr().
# Code here:
s8 = 65
print(f"the number of {s8} is {chr(s8)}")


# ------------------------------------------------------------
# 5. SLICING
# ------------------------------------------------------------

# 9. Print the first 5 characters of a string.
# Code here:
s9 = "Bro! you are doing great"
print(f"first 5 charcter are: {s9[0:5]}")

# 10. Reverse a string using slicing.
# Code here:
print(f"reverse string is : {s9[::-1]}")


# ------------------------------------------------------------
# 6. BUILT-IN STRING FUNCTIONS
# ------------------------------------------------------------

# Use the string: "  Python Programming  "

# 11. Use len() to print the number of characters.
# Code here:
s10 = "           string in python is good                "
print(len(s10))

# 12. Use strip(), lstrip(), and rstrip() — show the differences.
# Code here:
print(s10.strip())
print(s10.lstrip())
print(s10.rstrip())
# 13. Count how many times "o" appears.
# Code here:
s11 = "hey why you are in omegele you Programmatic women"
print(f"the 'o' in {s11} is {s11.count('o')}")

# 14. Use find() and index() to locate "P".
# Code here:

print(s11.find("P"))

for i in s11:
    if i == "P":
        print(f"index of P is {s11.index(i)}")

# 15. Check if the string is alphabetic using isalpha().
# Code here:

s12 = "hallo"
print(f"{s12} alphabetic result is {s12.isalpha()}")

# 16. Convert the string to uppercase and lowercase.
# Code here:

print(s12.lower())
print(s12.upper())

# 17. Split the string into a list of words.
# Code here:
s13 = s12.split()
print(s13)

# 18. Join a list ["I", "love", "Python"] into one string.
# Code here:
s14 = ["I", "love", "Python"]
s15 = " ".join(s14)
print(s15)

# 19. Replace "Python" with "Java" in the string.
# Code here:

s16 = s15.replace("Python", "Java")
print(s16)

# ============================================================
# END OF STRING EXERCISES FILE
# ============================================================
