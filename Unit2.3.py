#Widgets
#Oct 28
#Jessica B

#Input
w = int(input("Enter how many Disney Widgets you would like: "))
promo = raw_input("Enter a promo code if you have one: ")
promo = promo.lower()

#Calc
if w < 100 and promo == "crocs":
    ans = (.25 * w) *.1
    ans2 = round((.25 * w) - ans , 2)
    print w, "widgets will be $", ans2,"plus tax and shipping with the promo code"
elif w < 100:
    ans1 = round((.25*w),2)
    print w, "widgets will be $",ans1,"plus tax and shipping"
elif w >= 100 and promo == "crocs":
    ans3 = (.20 * w) * .1
    ans4 = round((.20 * w) - ans3, 2)
    print w,"widgets will be $",ans4,"plus tax and shipping with the promo code"
elif w >= 100:
    ans5 = round((.20*w),2)
    print w,"widgets will be $",ans5,"plus tax and shipping"
else:
    print "Invalid"
