import random
z = 0
while z == 0:
    
    a = int(input("Enter the highest possible value for the number: "))
    b = int(input("Enter the lowest possible value for the number: "))

    if a - b > 3:
        l = []
        l2 = l.insert(1,b)
        while b <> a:
            b = b + 1
            l3 = l.append(b)
            c = 0
        while c <> 3:
            c = c+1
            rd = random.choice(l)
            print rd, "is your unique number"
            re = l.remove(rd)
            z = z+1
        
    else:
        print "Invalid, range is too close"
            
