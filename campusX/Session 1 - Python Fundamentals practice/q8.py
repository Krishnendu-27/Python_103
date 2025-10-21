# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

# formulla : nth term=a+(n−1)⋅d

'''
a = first term
d = common difference = second term - first term
n = the term number you want to find
'''
a = int(input("enter first term"))
b = int(input("enter secoend term"))
d = b-a
n = int(input("enter nth term"))

nth = a+ (n-1)*d;

print("nth term " , nth);

