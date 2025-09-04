Matric=int(input("Enter your Matric marks out of 1100: "))
Inter=int(input("Enter your Inter marks out of 550: "))
Ecat=int(input("Enter your Ecat marks out of 400: "))


Result=((Matric*10/1100)+(Inter*40/550)+(Ecat*50/400))

print(f"The aggregate is {Result}%")
