#Averages
#Jan 9
#Jessica B

stud = ["joon cho","kelsey young","casey baker","austin morris","torrian pace","shannon dooley"]
score = [85.5, 94.5, 78, 64.5, 99, 91.5]


#Calc
low = min(score)
low2 = score.index(low)
low3 = stud[low2]
print "The lowest team score is:",low,"by",low3.title()
del score[low2]
del stud[low2]

high = max(score)
high2 = score.index(high)
high3 = stud[high2]
print "The highest team score is:",high,"by",high3.title()
del score[high2]
del stud[high2]

avg = round(sum(score) / len(score),2)
print "The average is:",str(avg)+"% minus the highest and lowest score"

#Input
n = raw_input("Enter a students first and last name: ")
s = float(input("Enter a students test score: "))
n2 = stud.insert(0,n)
s2 = score.insert(0,s)

#Calc
loww = min(score)
loww2 = score.index(loww)
loww3 = stud[loww2]
print "The lowest team score is:",loww,"by",loww3.title()
del score[loww2]

highh = max(score)
highh2 = score.index(highh)
highh3 = stud[highh2]
print "The highest team score is:",highh,"by",highh3.title()
del score[highh2]

avg2 = sum(score)/len(score)
avg3 = round(avg2 - avg,2)
print "The additional score increased the average by:",str(avg3)+"% points"


