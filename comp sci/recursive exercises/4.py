# Exercise 4: Reverse String
# Implement a function named reverse_string(s) that returns the reversed version of the string.
# Remember that the reverse of a string is the last character, concatenated with the reverse of
# the rest of the string.
# NOTE: You might need a recursive helper like in exercises 2 and 3.

def reverse_string_recursive_helper(word, index):
    if index < 0:
        return ""
    else:
        return word[index] + reverse_string_recursive_helper(word, index -1)

def reverse_string(word):
    return reverse_string_recursive_helper(word, len(word)-1)

# Test cases
print(reverse_string("hello"))    # Expected output: "olleh"
print(reverse_string(""))         # Expected output: ""
print(reverse_string("Python"))   # Expected output: "nohtyP"