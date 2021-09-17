def opt1():
    return 100 * 10

def opt2(y):
    while y <> 1024:
        y *= 2
    return y

def main():
    y = 1
    print "Option 1: The salary will be $"+str(opt1())
    print "Option 2: The salary will be $"+str(opt2(y))

    if opt1() > opt2(y):
        print "Option 1 is better for you"
    else:
        print "Option 2 is better for you"


main()
