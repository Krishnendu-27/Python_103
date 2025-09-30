# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
# formulla (a.d) + (b.c) / b.d
a = int(input("Enter first fraction numerator: "))
b = int(input("Enter first fraction denominator: "))
c = int(input("Enter second fraction numerator: "))
d = int(input("Enter second fraction denominator: "))

result = ((a * d) + (b * c)) / (b * d)

print("Sum of the two fractions is:", result)
