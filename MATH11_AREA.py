#ShapeArea
#Oct 4 19
#Jessica b

#Input
r = float(input("Enter the radius of the circle in feet: "))
b = float(input("Enter the base of the triangle in feet: "))
h = float(input("Enter the height of the triangle in feet: "))

#Calc
ans = 3.14 * (r**2)
ans2 = .5 * (b * h)

#Output
print "The area of the triangle is:",str(ans2), "square feet"
print "The area of the circle is:",str(ans),"square feet"
