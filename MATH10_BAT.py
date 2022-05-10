#Baseball
#Oct 1 2019
#Jessica b

#Input
name = raw_input("Enter the team's name: ")
name2 = raw_input("Enter the player's name: ")
won = float(input("Enter the total number of wins: "))
played = float(input("Enter the total number of games played: "))
tot = float(input("Enter the player's total number of at bats: "))
tot2 = float(input("Enter the player's total number of hits: "))
tot3 = float(input("Enter the player's total number of doubles: "))
tot4 = float(input("Enter the player's total number of triples: "))
tot5 = float(input("Enter the player's total number of home runs: "))

#Calc
per = round(won / played,3)
ave = round(tot2 / tot,3)
slug = round((tot2 - tot3 - tot4 - tot5)+(2 * tot3) + (3 * tot4) + (4 * tot5),3)
slug2 = round(slug/tot,3)


#Output
print "The",name,"'s winning percentage is:" , per *1000 ,"%"
print name2,"'s batting average is: ",ave* 1000,"%"
print "and their slugging percentage is: ",slug2*1000,"%"
