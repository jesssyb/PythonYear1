#RightTriangle
#Jessica B

sym = raw_input("Enter the symbol you want: ")
num = int(input("Enter the number of symbols at the base: "))


num1 = num + 1
for x in range(num):
    print sym
    num1 = num1-num
    for y in range(num1):
        if y <> num:
            print sym,
        else:
            print sym
        num1 +=1


        
