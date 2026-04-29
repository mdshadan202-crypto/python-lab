#Write a Python program to define a function that accepts two numbers and returns their greatest common divisor (GCD).
def find_gcd(a, b):
 while b != 0:
  a, b = b, a % b
  return a
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")
