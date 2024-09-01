def factorial_recursive(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def main():
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {num} is {factorial_recursive(num)}")

if __name__ == "__main__":
    main()
