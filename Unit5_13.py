num = int(input("Enter an odd number for the base: "))
for x in range(1,num+1,2):
    s = 1
    while s <= int((num-x)/2):
        print " ",
        s +=1
    for n in range(1,x+1):
        if n < x:
            print "*",
        else:
            print "*"
for y in range(1,num-2,2):
    z = 1
    while z <= int((num-x)/2):
        print " ",
        z +=1
    for c in range(1,x+1,2):
        if y > c:
            print "*"
        else:
            print "*",
            

