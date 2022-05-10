l = []
sv =""
pn = raw_input("Enter a phone number seperated using hyphens: ")
for x in range(12):
    pn1 = pn[x]
    pn2 = l.append(pn1)
print "The adjusted phone number is:",sv.join(l[0:3])+str(sv.join(l[4:7]))+str(sv.join(l[8:12]))
