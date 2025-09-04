name=input("Enter the student name: ")
Bio=int(input("Enter marks in Biology: "))
Chem=int(input("Enter the marks in chemistry: "))
Phy=int(input("Enter the marks in Physics: "))
Math=int(input("Enter the marks in Math: "))
English=int(input("Enter the marks in English: "))


Result=float((Bio+Chem+Phy+Math+English)/500)*100

print(f"The total percentage you get is {Result}%")