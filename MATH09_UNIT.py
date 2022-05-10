#UnitPrice
#Jessica B
#Sep 26 2019

#Input
price = float(input("Enter the price of the item: "))
pound = float(input("Enter the pounds of the item purchased: "))
ounces = float(input("Enter the total ounces of the item purchased: "))

#Calc
total = price/ ((pound * 16) + ounces)


#Output
print "The price per a ounce is: $", round(total, 2)
