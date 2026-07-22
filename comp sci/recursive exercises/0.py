# Exercise 0: Factorial
# Remember that n! is defined as n * (n-1)! and 0! is 1

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(0)) # Expected output: 1
print(factorial(1)) # Expected output: 1
print(factorial(2)) # Expected output: 2
print(factorial(3)) # Expected output: 6
print(factorial(4)) # Expected output: 24
print(factorial(5)) # Expected output: 120