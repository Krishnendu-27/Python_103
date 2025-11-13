# Sequence sum
# 1/1! + 2/2! + 3/3! + ...
n = 5
fact = 1
result = 0
for i in range(1, n):
    fact *= i
    result += i / fact

print(result)
