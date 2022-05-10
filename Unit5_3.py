#Bowling
#Jessica B

#Input
s = 0.0
c = 0
tot = 0.0
high = 0.0
low = 300.0
while s <> -1:
    s = float(input("Enter your bowling score, -1 to stop: "))
    if s <> -1:
        tot = tot + s
        c +=1
        if high < s:
            high = s
        if low > s:
            low = s
        
avg = round(tot/c,2)
print "The average is:",avg
print "The highest score is:",high
print "The lowest score is:",low
            
