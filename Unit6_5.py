def evenM5(num):
    if num % 5 == 0:
        return str(num)+" is not an even number or is a multiple of 5"
    else:
        return str(num)+" is an even number and not a mutiple of 5"

def main():
    num = int(input("Enter a whole number: "))

    print evenM5(num)
                
    
main()    
