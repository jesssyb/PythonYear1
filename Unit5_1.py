#Sum
#1/22
#Jessiac B

#Input
num1 = int(input("Enter a starting whole number: "))
num2  = int(input("Enter another ending whole number: "))

c = 0

while num1 <= num2:
    c = c+num1
    if num1 == num2:
        print str(num1),"=",c
    else:
        print str(num1),"+",
    
    num1 =num1+1
     


