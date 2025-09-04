t = (1, 2, 3, 2, 4, 2, 5)

print(t.count(2))   # 3 (since 2 appears three times)
print(t.count(5))   # 1
print(t.count(10))  # 0 (not present)


print(t.index(3))   # 2 (first occurrence of 3 is at index 2)
print(t.index(2))   # 1 (first occurrence of 2 is at index 1)
# print(t.index(10))  #  Error: ValueError (if item not found)

#other bulit-in functions for tuples
t = (1, 2, 3, 4, 5)
print(len(t))    # 5
print(min(t))    # 1
print(max(t))    # 5
print(sum(t))    # 15
print(sorted(t)) # [1, 2, 3, 4, 5] (returns a sorted list, not a tuple)
print(reversed(t)) # <reversed object> (returns an iterator)
print(tuple(reversed(t))) # (5, 4, 3, 2, 1) (to convert iterator to tuple)


