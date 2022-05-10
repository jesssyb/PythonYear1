#Jessica B
import random

card = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
val = [2,3,4,5,6,7,8,9,10,10,10,10,11]
suit = ["Hearts","Diamond","Spade","Clubs"]
tot = []
z = 0
 
val1 = random.choice(val)
val2 = random.choice(val)
tot1 = tot.append(val1)
tot2 = tot.append(val2)
print "You were dealt",card[val1-2],"of",random.choice(suit),"and",card[val2-2],"of",random.choice(suit),"for a total of:",sum(tot)
while z == 0:
    ask = raw_input("Do you want another card? Y or N: ")
    if ask.lower() == "y":
        for x in range(1):
            val3 = random.choice(val)
            tot3 = tot.append(val3)
            print "The new card is:",card[val3-2],"of",random.choice(suit),"for a total of:",sum(tot)
    else:
        z +=1
        if sum(tot) <= 21:
            print "You did not bust, your total was under 21"
        else:
            print "You busted, your total was over 21"
            
