marks=int(input("Enter your Marks: "))

if marks>=90:
    print("Your grade is A")
elif marks>=80 and marks<90:
    print("Your grade is B")    
elif marks>=70 and marks<80:
    print("Your grade is C")
elif marks<70:
    print("Your grade is D")
else:
    print("Invalid Marks")