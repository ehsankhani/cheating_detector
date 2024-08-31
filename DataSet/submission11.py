def custom_factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact

print(custom_factorial(5))
