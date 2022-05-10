#CostofCopies
#Nov 1
#Jessica B

#Input
c = int(input("Enter how many copies you would like: "))
cs = raw_input("Would you like card stock? Yes or No: ")
cs = cs.lower()

#Calc
if c >= 101 and cs == "yes":
    ans1 = round(((100*.08) + (.06 * (c-100))),2)
    print "The total cost is: $"+str(ans1)
elif c >=101 and cs == "no":
    ans2 = round(((100 * .08) + (.06 * (c-100))),2)
    print "The total cost is: $"+str(ans2)
elif c <= 100 and cs == "yes":
    ans3 = (.08 * c)
    print "The total cost is: $"+str(ans3)
elif c <= 100 and cs == "no":
    ans4 = (.05 * c)
    print "The total cost is: $"+str(ans4)
else:
    print "Invalid"
