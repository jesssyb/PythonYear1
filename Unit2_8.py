#Costco
#Nov 18
#Jessica B

#Input
bill = float(input("Enter the total amount of your Costco bill: "))
ten = (bill * .1)

#Calc
if bill <= 500:
    print "You do not qualify for the discount"
elif bill >= 501 and ten < 100:
    print "10% off your bill is $"+str(ten),"therefore you select the $100"
elif bill >= 501 and ten > 100:
    print "10% off your bill is $"+str(ten),"therefore you select the 10% discount"
elif bill >=501 and ten == 100:
    print "10% off your bill is $"+str(ten),"the same as the $100 cashback"
else:
    print "Invaild"
    
