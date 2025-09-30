# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
# formulla d = √[(x₂ - x₁)² + (y₂ - y₁)²]

x1 = int(input("enter 1st cordinate: "))
y1 = int(input("enter 1st cordinate: "))
x2 = int(input("enter 2nd cordinate: "))
y2 = int(input("enter 2nd cordinate: "))

result = ((((x2 - x1)**2)  + ((y2 - y1)**2)) ** 0.5);

print(result)