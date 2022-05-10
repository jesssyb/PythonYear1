#GiftList
#Dec 18
#Jessica b

#Input
gift = ["Lionel Mega Tracks", "Lil Lockitz", "BFF Necklace", "Xbox", "Hoverboard", "I-Phone X"]
cost = [49.99, 34.99, 24.99, 249.00, 299.99, 649.99]

toy = raw_input("Enter a toy: ")

if toy in gift:
    print "The cost of the toy is: ",
else:
    print "Sorry your toy is not on our list."
    g = gift.append(toy)
    c2 = raw_input("Enter the cost of the toy: ")
    c3 = cost.append(c2)
    print "The cost of the",toy,"is: ",
