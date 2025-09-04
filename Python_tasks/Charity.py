Movie=input("Enter the name of Movie: ")
Adult=int(input("Enter the number of Adult tickets sold: "))
Child=int(input("Enter the number of Children tickets sold: "))
Price1=int(input("Enter the Price for Adult ticket: "))
Price2=int(input("Enter the Price of Child ticket: "))

Percent=int(input("Enter the percentage you want to charity: "))

Total_Price=int((Adult*Price1)+(Child*Price2))
# print(Total_Price)
Donation=(Total_Price*Percent)/100
# print(Donation)
Profit=Total_Price-Donation
# print(Profit)
Result1=print(f"The amount of Charity is {Donation}%")
Result2=print(f"The amount of Profit after donation is {Profit}%")
