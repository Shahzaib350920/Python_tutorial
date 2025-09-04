#Take any three movies and store them ina list.

mov1=input("Enter your first movei name: ")
mov2=input("Enter your second movie name: ")
mov3=input("Enter your third movie name: ")

list=[]

list.append(mov1)
list.append(mov2)
list.append(mov3)

print("Your favourite movies are: ", list)


#Question 2

list=[]

val1=input("Enter your first value: ")
val2=input("Enter your second value: ")
val3=input("Enter your third value: ")
val4=input("Enter your fourth value: ")
val5=input("Enter your fifth value: ")

list.append(val1)
list.append(val2)
list.append(val3)
list.append(val4)
list.append(val5)

print("The list is: ", list)

list1=list.copy()

list1.reverse()

if list==list1:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")