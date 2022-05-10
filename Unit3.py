#Assignment
#Jessica B
#Nov 25

#Input
n = raw_input("Enter the full name of a College or University: ")
l = raw_input("Enter a letter: ")
n = n.lower()

#Calc
t1 = len(n)
print "The length of the string is:",t1

t2 = l.find(l)
t3 = n.rfind(l)

if t2 >= 0:
    print "The letter" ,l,"appears at index",t3
else:
    print l,"does not appear in",n

print "The first letter is:",n[0]
print "The last letter is:",n[-1]

first = n[0]
sp = n.find(" ")
mid = n[sp+1]
n2 = n[sp+1:] 
sp2 = n2.find(" ")
last = n2[sp2 + 1]
print first.upper() + mid.upper() + last.upper()
