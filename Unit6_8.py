def main():
    fn = raw_input("Enter your first name: ")
    ln= raw_input("Enter your last name: ")
    sal = float(input("Enter your annual salary: "))

    if sal <=40000:
        print "The new salary for",fn,"",ln,"is:",less(sal)
    else:
        print "The new salary for",fn,ln,"is:",more(sal)
    

def less(sal):
    return(sal * .05) + sal
    

def more(sal):
    return round((sal+2000)+ (40000 * .02),2)

    

main()

    
    
