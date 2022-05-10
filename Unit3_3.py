#Name
#Dec 4
#Jessica B

#Input
n = raw_input("Enter your first and last name: ")
n = n.lower()


sp = n.rfind(" ")
last = n[sp+1: ]
f = n.find(" ")
f2 = n[0:sp+1]

print "Reverse order is:",last.title()+str(","),f2.title()

n2 = raw_input("Enter your first, middle, and last name:")

sp = n.rfind(" ")
last = n[sp+1: ]
f = n.find(" ")
f2 = n[0:sp+1]
f3 = n[f+1:sp+1]

print "Your middle name is:",f3.title()
