#AreaofCirlce
#Oct 22
#Jessica B

#Input
r = float(input("Enter the radius of the circle: "))

#Calc
if r > 0:
    ans = round(3.14 * r * r,2)
    print "The area of the circle is:",ans,"squared units"
else:
    print "The radius is invalid please enter a value greater than zero"
