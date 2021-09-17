#Letter grade

#input
def main():
    tg = inputgrade()
    print "The letter grade is: "+str((tg))
    
def inputgrade():
    tg = int(input("Enter the test grade: "))
    return lettergrade(tg)

def lettergrade(tg):
   if tg >= 91:
       return "A"
   elif tg >= 81:
        return "B"
   elif tg >= 71:
        return "C"
   elif tg >=61:
        return "D"
   else:
        return "F"
    

main()


             
