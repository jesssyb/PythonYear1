#Jessica
#Pyramid

num = int(input("Enter a odd number: "))

row = 1
for x in range(1,num+1,2):
    s=1
    while s <= int((num-x)/2):
        print " ",
        s+=1
        print row
    for n in range(1,x+1):
        if n < x:
            print "*",
        else:
            print "*"
    row +=1
    print
    

        
        
        
        
    
    

