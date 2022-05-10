#WinLose
#Oct 15
#Jessica B

#Input
t = raw_input("Enter the team's name: ")
s = int(input("Enter the score for" (t)+ ": "))
t1 = raw_input("Enter the other team's name: ")
s1= int(input("Enter"+t1+"'s score: "))

#Calc
if s > s1:
    print t, "was the winner, they beat",t1,"by a score of",s, "to", s1
else:
    print t1, "was the winner, they beat",t,"by a score of",s,"to",s1
