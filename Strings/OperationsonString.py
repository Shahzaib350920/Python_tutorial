#String Indexing 

word = "Python"
print(word[0])   # P  (first char)
print(word[-1])  # n  (last char)
print(word[2])   # t
print(word[-2])  # o


#String Concatenation

a = "Python"
b = "Programming"
print(a + " " + b)   # Python Programming
print(a + b)         # PythonProgramming


#String Slicing

text = "Hello World"

print(text[0:5])   # Hello   (from index 0 to 4)
print(text[:5])    # Hello   (start default = 0)
print(text[6:])    # World   (end default = last)
print(text[-5:])   # World   (last 5 chars)
print(text[:])     # Hello World (full string)


