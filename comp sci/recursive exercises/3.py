# Exercise 3: Count Vowels
# Develop a function called count_vowels(string) to count the number of vowels in the provided string.
# You can assume the string will be entirely lowercase.
# Remember that the count of vowels in a string is the number of vowels (0 or 1) in the first character
# plus the number of vowels in the rest of the string.
# NOTE: you will also need to implement a recursive helper, like in exercise 2.

vowels = "aeiou"
def count_vowels_recursive_helper(word, index):
    if index == len(word):
        return 0
    elif word[index] in vowels:
        return 1 + count_vowels_recursive_helper(word, index + 1)
    else:
        return count_vowels_recursive_helper(word, index + 1)

def count_vowels(word):
    return count_vowels_recursive_helper(word, 0)

# Test cases
print(count_vowels("hello"))     # Expected output: 2
print(count_vowels("python"))    # Expected output: 1
print(count_vowels("aeiou"))     # Expected output: 5
