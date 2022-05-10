#WhiteBoardProblem1
#Sep. 17 1029
#Jessica B

#Input

n = float(input("Enter a whole number: "))
d = float(input("Enter a whoe number: "))

#Calc
ans = n / d
rem = n%d

#Output
print "The answer is" ,ans, "with a remainder of" ,rem

#WhiteBoard2

#Input
students = int(input("Enter the number of students going on the trip: "))

#Calc
hold = 48
ans1 = students / hold
ans2 = students % hold
ans3 = students - ans2

#Output
print round(ans1), "buses are needed to take" , ans3, "students on the trip." , ans2, "students will be left behind because there is not enough room on the bus."


#Whiteboard3

#Input
cookies = int(input("Enter the number of cookies you made: "))

#Calc
containers = 12
ans4 = cookies / containers
ans5 = cookies % containers

#Output
print "You need", ans4, "containers for the cookies, there are" , ans5, "cookies left for you to eat."
