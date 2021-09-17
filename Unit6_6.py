def one(m):
    return (m * 2.54)

def two(m):
    return (m * 30)

def three(m):
    return (.91 * m)

def four(m):
    return (m * 1.6)

def five(m):
    return(m/2.54)

def six(m):
    return(m/30)

def seven(m):
    return(m/.91)

def eight(m):
    return(m/1.6)

def main():
    m = float(input("Enter the measurement: "))
    print "1 - Inches to Centimeters"
    print "2 - Feet to Centimeters"
    print "3 - Yards to Meters"
    print "4 - Miles to Kilometers"
    print "5 - Centimeters to Inches"
    print "6 - Centimetes to Feet"
    print "7 - Meters to Yards"
    print "8 - Kilometers to Miles"
    sec = int(input("Enter the number of your selection: "))
    if sec == 1:
        print "There are",one(m),"centimeters in",m,"inches"
    elif sec == 2:
        print "There are",two(m),"centimeters in",m,"feet"
    elif sec == 3:
        print "There are",three(m),"meters in",m,"yards"
    elif sec ==4:
        print "There are",four(m),"kilometers in",m,"miles"
    elif sec == 5:
        print "There are",five(m),"inches in",m,"centimeters"
    elif sec == 6:
        print "There are",six(m),"feet in",m,"feet"
    elif sec == 7:
        print "There are",seven(m),"yards in",m,"meters"
    elif sec == 8:
        print "There are",eight(m),"miles in",m,"kilometers"
    else:
        print "Invalid"
main()
