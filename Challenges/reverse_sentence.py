def reverse_sentence(string):
    listStr = string.split(' ')[::-1]
    res = ' '.join(listStr)
    return res


print(reverse_sentence("Hello world!"))  # Output: "world! Hello"
print(reverse_sentence("Python is awesome"))  # Output: "awesome is Python"
