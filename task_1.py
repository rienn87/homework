def factorial(value):
    res = 1
    for i in range(1, 1+value):
        res *= i
    return res

print(factorial(1))