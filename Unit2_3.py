#Bagels
#Oct 25
#Jessica B

#Input
bagel = int(input("Enter the number of bagels you ordered: "))
cc = raw_input("Do you want cream cheese?($0.35 per bagel): ")
cc = cc.lower()

#Calc
if bagel >= 6 and cc == "yes":
    ans = round((.6 * bagel) + (.35 * bagel),3)
    print "You ordered",bagel, "bagels with cream cheese. The total cost is: $"+str(ans)
elif bagel >= 6 and cc == "no":
    ans1 = round((.6 * bagel),3)
    print "You ordered",bagel,"bagels without cream cheese. The total cost is: $"+str(ans1)
elif bagel < 6 and cc == "yes":
    ans2 = round((.75 *bagel) + (.35 * bagel) ,3)
    print "You ordered",bagel,"bagels with cream cheese. The total cost is: $"+str(ans2)
elif bagel < 6 and cc == "no":
    ans3 = round((.75 * bagel),3)
    print "You ordered",bagel,"bagels without cream cheese. The total cost is: $"+str(ans3)
else:
    print "Invaild input"
