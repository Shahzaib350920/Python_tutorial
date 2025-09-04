# Examples of tuples
t1 = ()                       # Empty tuple
t2 = (1, 2, 3, 4, 5)          # Tuple with integers
t3 = ("apple", "banana", 3.14, True)  # Mixed data types
t4 = (1,)                     # Single-element tuple (notice the comma!)
t5 = (1, 2, (3, 4, 5))        # Nested tuple


#Slcicing in tuples

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])   # (20, 30, 40)
print(numbers[:3])    # (10, 20, 30)
print(numbers[2:])    # (30, 40, 50, 60)
print(numbers[::-1])  # (60, 50, 40, 30, 20, 10) → reversed
print(numbers[::2])   # (10, 30, 50) → step of 2


#Tuples vs List 

# Lists are mutable (can be changed), tuples are immutable (cannot be changed)
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list[0] = 10      # ✅ Valid
# my_tuple[0] = 10   # ❌ Error: TypeErroprint
print(my_list)   # [10, 2, 3]
print(my_tuple)  # (1, 2, 3)


