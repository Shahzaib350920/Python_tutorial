
#Question 1

#Check if the number is odd or even 

num =int(input("Enter a number: "))
if num%2==0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")


#Question 2

#Write a program  to find the lagest of the 3 numbers


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))


if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and (num2>=num3): 
    largest=num2
else:
    largest=num3

print("The largest number is: ", largest)


#Question 3

#Check if the number is divisible by 7 or not

Num=int(input("Enter a number: "))
if Num%7==0:
    print(Num, "is divisible by 7")
else:
    print(Num, "is not divisible by 7")