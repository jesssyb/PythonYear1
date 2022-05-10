#MakeChange
#Sep. 18, 2019
#Jessica B

#Input
change = int(input("Enter the amount of change: "))

#Calc
q = change / 25
q2 = change % 25
d = q2 / 10
d2 = q2 % 10
n = d2 / 5
p = d2 % 5


#Output
print "Quarters: ", q
print "Dimes: " , d
print "Nickels: ", n
print "Pennies: ", p


