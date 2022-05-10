#New Years
#Jan 6
#Jessica B

#Resubmission

#Input
resolution = ["exercise more","lose weight","eat healthier","stop smoking","more family time"]
broken = ["lose weight","stop smoking","eat healthier","more family time","save money"]

res = raw_input("Enter your resolution: ")
res1 = res.lower()

#Calc
if res1 not in resolution and res1 not in broken:
    print "Your resolution was not in either of the lists"
    print res1.title(),"has been to the resolution list"
    add = resolution.append(res1)
elif res1 in resolution:
    if res1 in broken:
        print res1.title(),"is in the top 5 lists for made and broken resolutions"
    else:
        print res1.title(),"is in the top 5 lists for made resolutions"
elif res1 in broken:
    if res1 in resolution:
        print res1.title(),"is in the top 5 lists for made and broken resolutions"
    else:
        print res1.title(),"is in the top 5 lists for broken resolutions"
        
        
