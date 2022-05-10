#DeskProject
#Sep. 12 2019
#Jessica B

#Input
name = raw_input("Enter the teacher's name: ")
room = raw_input("Enter the room number: ")
length = float(input("Enter the length of the room(ft): "))
width = float(input("Enter the width of the room(ft): "))
desk = 20

#Calc
ans = length * width
ans1 = (length * width)/ desk

#Output
print "Room number" , room, "taught by" ,name, "has an area of", ans, "squared feet."
print "The room holds a total of" , int(ans1), "desks."
