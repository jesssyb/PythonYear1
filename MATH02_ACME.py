#Profit_Calc
#Sep. 6, 2019
#Jessica B Pd. 3

#Input
each = float(input("Enter the production cost per item: "))
whole = float (input("Enter the sales price per item: "))
total = int(input("Enter the total amount ordered: "))

#Calc
ans = whole - each
ans2 = total * ans

#Output
print "The Acme company makes $", ans, "per widget"
print "Therefore on a sale of", total, "widgets, they made $" , ans2

