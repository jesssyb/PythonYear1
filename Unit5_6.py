#Jessica B

#Input
z = 0
high = 0.0
while z == 0:
    for x in range(1,4):
        num = float(input("Enter a positive number: "))
        z +=1
        if high < num:
            high = num
        
    print "The largest number of the three is:",high
        
        
    
    
    
