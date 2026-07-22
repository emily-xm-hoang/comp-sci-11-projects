# Exercise 1: Power Function
# Create a function called power(x, y) that calculates x raised to the power of y (x^y).
# Remember that x^y is defined as x * x^(y-1) and x^0 is 1.

def power(x, y):
    if y == 0:
        return 1
    else: 
        return x*power(x, y - 1)

# Test cases
print(power(2, 3))  # Expected output: 8
print(power(5, 0))  # Expected output: 1
print(power(3, 2))  # Expected output: 9