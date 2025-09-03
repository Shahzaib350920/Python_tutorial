# Original list
list1 = [12, 13, 14, 11, 55, 66, 77, 34, 54]
print("Original list:", list1)

# Append 765 at the end
list2 = list1.copy()
list2.append(765)
print("After append(765):", list2)

# Sort list in ascending order
list3 = list2.copy()
list3.sort()
print("After sort() ascending:", list3)

# Sort list in descending order
list4 = list2.copy()
list4.sort(reverse=True)
print("After sort(reverse=True):", list4)

# Reverse the list (not the same as descending sort, just flips order)
list5 = list4.copy()
list5.reverse()
print("After reverse():", list5)

# Insert 5 at index 4
list6 = list5.copy()
list6.insert(4, 5)
print("After insert(4, 5):", list6)


fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")   # removes the first "banana"
print(fruits)             # ['apple', 'cherry', 'banana']

# fruits.remove("grape")  # ❌ Error: ValueError (if item not found)


numbers = [10, 20, 30, 40, 50]

x = numbers.pop()     # removes last element (50)
print("Popped:", x)   # Popped: 50
print(numbers)        # [10, 20, 30, 40]

y = numbers.pop(1)    # removes element at index 1 (20)
print("Popped:", y)   # Popped: 20
print(numbers)        # [10, 30, 40]
