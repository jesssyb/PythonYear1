#Review

#Input
print "Part One"
hh = "Happy holidays"
nw = "New Year"
nw2 = hh.replace("holidays",nw)
print hh
print nw2

print "Part Two"
sp = nw2.find(" ")
print "The first location of a space in",nw2,"is: index ",sp

print "Part Three"
f = nw2[0:sp+1]
print "The first word is:",f

print "Part Four"
bd = raw_input("Enter the word birthday: ")
if bd == "birthday":
    n = raw_input("Enter your name: ")
    bd = bd.lower()
    n = n.lower()
    bd2 = nw2.replace("New Year", bd)
    print bd2.title(),n.title()
else:
    print "Invalid"
