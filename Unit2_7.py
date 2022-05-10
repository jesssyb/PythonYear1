#HighLow
#Nov 15
#Jessica B

#Input
num1 = int(input("Enter a whole number: "))
num2 = int(input("Enter a whole number: "))
num3 = int(input("Enter a whole number: "))

#Calc
if num1 > num2 and num1 > num3:
    print "The greatest number is: "+str(num1)
elif num2 > num1 and num2 > num3:
    print "The greatest number is: "+str(num2)
elif num3 > num1 and num3 > num2:
    print "The greatest number is: "+str(num3)
else:
    print "Invaild"

if num1 < num2 and num1 > num3:
    print "The middle number  is: "+str(num1)
elif num1 > num2 and num1 < num3:
    print "The middle number is: "+str(num1)
elif num2 > num1 and num2 < num3:
    print "The middle number is: "+str(num2)
elif num2 < num1 and num2 > num3:
    print "The middle number is: "+str(num2)
elif num3 < num1 and num3 > num2:
    print "The middle number is: "+str(num3)
elif num3 > num1 and num3 < num2:
    print "The middle number is: "+str(num3)
else:
    print "Invaild"

if num1 < num2 and num1 < num3:
    print "The lowest number is: "+str(num1)
elif num2 < num1 and num2 < num3:
    print "The lowest number is: "+str(num2)
elif num3 < num1 and num3 < num2:
    print "The lowest number is: "+str(num3)
else:
    print "Invaild"

#Output
if num1 > num2 > num3:
    ans1 = round(((num1 + num2) * 1.0)/2,2)
    print "The average of the two highest numbers is: "+str(ans1)
elif num1 > num2 < num3:
    ans2 = round(((num1 + num3)* 1.0)/2,2)
    print "The average of the two highest numbers is: "+str(ans2)
elif num1 < num2 < num3:
    ans3 = round((((num3 + num2)* 1.0)/2),2)
    print "The average of the two highest numbers is: "+str(ans3)
elif num1 < num2 > num3 and num1 > num3:
    ans4 = round((((num2 + num1)* 1.0)/2),2)
    print "The average of the two highest numbers is: "+str(ans4)
elif num1 < num2 > num3 and num1 < num3:
    ans5 = round((((num2 + num3)* 1.0)/2),2)
    print "The average of the two highest numbers is: "+str(ans5)
