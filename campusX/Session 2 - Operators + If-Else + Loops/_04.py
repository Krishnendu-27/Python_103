# loops in python
# loop use in showing product example flipcart , amazon , swiggey 
n = int(input("enter the number"));
m = 0;
while(n!=0):
    n = int(input("enter the number"));
    m = n
print(m)
# we can use else in loop also 

x = 1
while x<5:
    print(x)
    x += 1;
else:
    print("limited crosssssss")

# guessing game
import random
rand = random.randint(1,10)
# n = int(input("enter the number "))
n = 0;
count = 0;
while(n != rand):
    if n > rand:
        n = int(input("enter the number "))
        print("you guess higher than actual number. guess lower");
        count += 1;
    else:
        n = int(input("enter the number "))    
        print("you guess lower than actual number. guess higher");
        count += 1;
else:
    print("You guess correct in " , count , "chance");
# -----------------------------------
# for loop
# it use a function called range
# for i in range(first number, till it goes,step size(itration it will go)):
for i in range(1, 10+1 , 2):
    # in range it goges 1 to n-1 so we add 1 
    print(i)
for i in range(10, -1 , -1):
    print(i)

for i in 'DELHI':
    print(i);
# we can do loop in everything it flexiable to use