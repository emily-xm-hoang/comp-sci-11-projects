# Exercise 2: Sum of Integers
# Write a function named sum_list_recursive(numbers, index) that
# Takes a list of integers and an index and returns their sum.
# Remember that the sum of a list is the first item plus the sum of the rest of the list.

def sum_list_recursive_helper(numbers, index):
    if index == len(numbers):
        return 0
    else: 
        return numbers[index] + sum_list_recursive_helper(numbers, index + 1)

def sum_list(numbers):
   return sum_list_recursive_helper(numbers, 0)

# Test cases
print(sum_list([1, 2, 3, 4]))   # Expected output: 10
print(sum_list([-1, 1, 2]))     # Expected output: 2
print(sum_list([5, 10, 15]))    # Expected output: 30