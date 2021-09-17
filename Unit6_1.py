#Mail Prices

#Input the weight
def main():
    w = float(input("Enter the weight: "))
    p = cost(w)
    print "The cost is mail the letter is: $"+str(p)
   
def cost(w):
    nw = ceil(w)
    print "Adjusted weight:",nw
    cost1 = ((nw - 1) *.1)+.05
    return cost1

def ceil(w):
    if w >int(w):
        return(int(w)+1)
    else:
        return int(w)
    

main()
        
