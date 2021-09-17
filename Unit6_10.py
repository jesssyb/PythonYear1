def calc(i,pay,bal):
    ip = (bal * (i/100))/12
    rp = pay - ip
    fb = bal - rp
    return display(ip,rp,fb)
   
def display(ip, rp,fb):
    print "Interest paid:",round(ip,2)
    print "Reduction of principal:",round(rp,2)
    print "End of month balance:",round(fb,2)

def enter():
    i = float(input("Enter the annual rate of interest: "))
    pay = float(input("Enter the monthly payment: "))
    bal = float(input("Enter the balance from the beginning of the month: "))
    return calc(i,pay,bal)

enter()
