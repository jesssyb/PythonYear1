#Max and Min

def minnum(num):
    minval = num[0]
    for index in num:
        if index < minval:
            minval = index
    return minval

def maxnum(num):
    maxval = num[0]
    for index in num:
        if index > maxval:
            maxval = index
    return maxval

def main():
    list0 = []
    yon = "y"
    while yon.lower()== "y":
        input0 = int(input("Enter a number: "))
        input0 = list0.append(input0)
        yon = raw_input("Input another number? Y or N: ")

    print "Min value:",(minnum(list0))
    print "Max value:",(maxnum(list0))

main()
        
