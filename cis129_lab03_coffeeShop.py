#Program made by James Glaser for 21226 CIS129 Programming and Problem Solving I 
#Started February 18, 2025 @ 3:38PM

#Display name of coffee shop and ask what you will be buying
print("***************************************")
print("My Coffee and Muffin Shop\n")
print("Number of coffees bought?")
coffeesBought = int(input())
print("\nNumber of muffins bought?")
muffinsBought = int(input())
print("***************************************\n\n***************************************")

#Declaring variables to calculate the total cost
costPerCoffee = 5.00
costPerMuffin = 4.00
coffeeTotalCost = coffeesBought * costPerCoffee
muffinTotalCost = muffinsBought * costPerMuffin
subtotal = coffeeTotalCost + muffinTotalCost
tax = subtotal * 0.06
taxTotal = subtotal * 1.06

#showing totals and tax
#I used f strings to get the program to display precise prices on the receipt
print("My Coffee and Muffin Shop Receipt")
if coffeesBought > 1:
    print(str(coffeesBought) + " Coffees at $5 each: $" + f"{coffeeTotalCost:.2f}")
else:
    print(str(coffeesBought) + " Coffee at $5 each: $" + f"{coffeeTotalCost:.2f}")
if muffinsBought > 1:
    print(str(muffinsBought) + " Muffins at $4 each: $" + f"{muffinTotalCost:.2f}")
else:
    print(str(muffinsBought) + " Muffin at $4 each: $" + f"{muffinTotalCost:.2f}")
print("6% tax: $" + f"{tax:.2f}")
print("---------")
print("Total: $" + f"{taxTotal:.2f}")
print("***************************************")
