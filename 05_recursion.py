# Program to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("enter a number to calculate its factorial:"))
print(f"Factorial of {num}:", factorial(num))
