# found population end of the last year if today population is 10000
'''
formulla:
population of 9th year = x
x + 10% of x = 10000
x+0.1x = 10000
1.1x = 10000
x = 10000/1.1
'''
current_pop = 10000
for i in range (10 , 0 , -1):
    current_pop = current_pop/1.1;
    print(f"in the previous year {i} population is {current_pop}")

# find the sum of 1/1! + 2/2! + 3/3! till n term

n = int (input("enter the n: "));

result = 0
fact = 1
for i in range(1,n+1):
    fact *= i
    result += i / fact
print(result)