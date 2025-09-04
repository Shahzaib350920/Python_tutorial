fruit=float(input("Enter the price of vegtable per kg in coins: "))
vegetable=float(input("Enter the price of fruits per kg in coins: "))
weight1=int(input("Enter the weight of the vegetable: "))
weight2=int(input("Enter the weight of the fruit: "))

Total=(fruit*weight2)+(vegetable*weight1)
print(f"The price of vegetable and fruit is {Total} coins")

ConvertintoRupee=Total/1.94

print(f"The Price of fruits and vegetables is {ConvertintoRupee} Rupee")
