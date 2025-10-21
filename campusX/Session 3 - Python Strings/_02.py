# nested loop
# its bacicaly we run loop in a loop
for i in range (0,2):
    # without compleing child loop parrent loop can not work
    for j in range(0,2):
        print(i,j);

# pattern 1
'''
*
**
***
'''
for i in range(1,5):
    for j in range(1,i):
        print("*" , end=" ")
    print()
# pattern 2
'''
1
121
12321
1234321
'''
for i in range(1,5):
    for j in range(1,i):
        print(j, end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    print()
