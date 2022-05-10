#angrybirds
#jan 25
#Jessica B

#Input
score = 0
avg = 0
el = []
while score >= -1:
    score = float(input("Enter your Angry Birds score or -1 to quit: "))
    el1 = el.append(score)
    avg = avg+1
    if score == -1:
        avg1 = avg-1
        el2 = sum(el)+1
        print 
        print "The average score is:",round(el2/avg1,2)
        break
    
