#Paycheck
#Sep. 20 2019
#Jessica B

#Input
sal = int(input("Enter the beginning salary: "))

#Calc
ras = (sal * .10) + sal
cut = ras - (ras *.1)
per = round((cut-sal) / sal,2)*100


#Output
print "Salary after 10% pay raise: ", ras
print "Salary after 10% pay cut: ", cut
print "Percentage change from original salary to final salary: ", per
