#TimeandHalf
#Nov 7
#Jessica B

#Input
name = raw_input("Enter the employee's name: ")
hours = float(input("Enter the hours he worked: "))
wage = float(input("Enter the hourly wage: "))

#Calc
if hours >= 41:
    gp = (40*wage) +((hours - 40) * (1.5 * wage))
    print name,"made $"+str(gp)
elif hours <=40:
    gp2 = (hours * wage)
    print name,"made $"+str(gp2)
