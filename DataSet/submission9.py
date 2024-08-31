def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

fibo_result = fib(10)
print("10th Fibonacci number:", fibo_result)
