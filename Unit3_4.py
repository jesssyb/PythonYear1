#Twitter
#Dec 5
#Jessica

#Input
n = raw_input("Enter the name of the high school, not including high school:")
n2 = int(input("Enter the words in the name: "))
sm = raw_input("Enter the school's mascot: ")
n = n.lower()
sm = sm.lower()

#Calc
sp = n.find(" ")
if sp == 0 and n2 >= 2:
    first = n[0:sp+1]
    tn = n[sp+1: ]
    tn2 = first + tn
    print first,"is the first name of your high school"
    print "@"+str(tn2),"is the new twitter name"
    
elif sp == 0 and n2 <=1:
    print "Invaild 3"
    
elif sp == -1 and n2 == 1:
    print "The first name of your highschool is:",n
    print "@"+str(n+sm),"is your new twitter name"
    
elif sp == -1 and n2 >= 2:
    print "Invaild 2"
    
    
    
    
