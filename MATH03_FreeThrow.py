#FreeThrowProject
#Sep. 10, 2019
#Jessica B

#Input
name = raw_input("Enter the player's name: ")
attempt = float(input("Enter the player's number of attempts: "))
made = float(input("Enter the player's number of made free throws: "))

#Calc
ans = round((attempt - made)/attempt, 2)*100

#Output
print name, "has made" ,int(ans), "% of their free throws"
