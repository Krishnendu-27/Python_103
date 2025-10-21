# operator in python 

#1. arthmetic operator + - * / % 
# // it give output in intiger not decomal
# ** power of operator it give  power
print(5+6)
print(5-6)
print(5*6)
print(5/6)
print(5//6)
print(5**6) # power of 6
#2. re;ational operator
print(4>5) # false is 4 big after 5
print(4<5) # true
print(4>=5) # false is 4 big from 5
print(4<=5) # true
print(4==5) # false
print(4!=5) #  true becuse 4 and  are not same 
#3. logical operator
# and both need to match the condtion
print(1<5 and 5>1) # true 
# or any one need to match the condtion
print(1>5 or 5>1) # true 
# not it reverse the condition condtion
print( not True) 

# 4. bit wise operator it work on binary conditon
# bitwise and
print(2&3)
# now it do "and" each one
# logic behind is 
'''
Compare each bit in two numbers.
Keep the bit as 1 only if both bits are 1.
Otherwise, it becomes 0.
'''
# 1 0 = 2
# 1 1 = 3
# 1 0 = 2

# bitwise or
print(2|3)
# now it do "or" each one
# logic behind is 
'''
Compare each bit in two numbers.
Keep the bit as 0 only if both bits are 1.
Otherwise, it becomes 1.
# reverse of and
'''
# bitwise Xor
print(2 ^ 3)
# logic behind is 
'''
Compare each bit in two numbers.
Keep the bit as 0 only if both bits are same.
mens if 1 ^ 1 = 0 , 0 ^ 0 = 0
Otherwise, it becomes 1.
mens if 1 ^ 1 = 1 ,  1^ 0 = 1
'''
# 1 0 = 2
# 1 1 = 3
# 0 1 = 

# bitwise not
print(~5) 
# logic behind is 
'''
Decimal: 5
Binary:  00000101
then add 1 
ans is:  00000110 
Flip the bits:
11111010 → 00000101
Add 1:
00000101 + 1 = 00000110 = 6
Add the minus sign → -6
so ~5 = -6
''' 
# Bitwise left shift
print(5 << 1)
# logic behind is:
'''
Decimal: 5
Binary:  00000101
Left shift by 1:
→         00001010
Which is: 10 in decimal
So 5 << 1 = 10
'''

# Bitwise right shift
print(5 >> 1)
# logic behind is:
'''
Decimal: 5
Binary:  00000101
Right shift by 1:
→         00000010
Which is: 2 in decimal
So 5 >> 1 = 2
'''
''' code logic is 
5 << 2 = 5 * (2 ** 2) = 20 
5 >> 1 = 5 // (2 ** 1) = 2
'''

# 4. assingment operator 
# = is called assingment operator
a = 10
print(a)
#  += it work like a = a +10
a += 10
print(a)
#  -= it work like b = b-10
a -=10 
print(a)
#  %= it work like b = b%10
a %=2 
print(a)
# a++ and ++a not work in python

# 5. membership operator
# in / not in
# it work in list tuple dictnoray
print('G' in 'Ghosh') # true
print( 5 in [1,2,3,6,4]) # false
print( 10 not in [1,2,3,6,4]) # false

# find the sum of 3 number enter by user
num = int(input("enter the number"))
sum = 0;
# without loop
# temp = num 
# a = temp % 10;
# temp = temp // 10;
# b = temp % 10;
# temp = temp // 10;
# c = temp % 10;
# temp = temp // 10;
# print(a+b+c)
while(num!=0):
    r = num % 10;
    sum = sum + r;
    num = num//10;
print(sum)

