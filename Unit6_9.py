def main():
    ob = float(input("Enter old balance: "))
    nc = float(input("Enter new charges: "))
    pay = float(input("Enter payment: "))
    nb = (nc - pay) + ob + (.015 * ob)

    print "New Balance is:",nb
    print "Mininum payment is:",display(ob,nc,pay,nb)

def display(ob,nc,pay,nb):
    if nb <= 20:
        return nb
    else:
        return 20 +((nb-20)*.1)

main()
