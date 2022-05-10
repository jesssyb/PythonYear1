#Replace
#Dec 2
#Jessica B

#Input
s = raw_input("Enter a sentence: ")
r = raw_input("Enter a word from the sentence to be replaced: ")
r2 = raw_input("Enter the word to be placed in the sentence: ")

#Calc
ans = string.replace(r,r2)

#Output
print "The origianl sentence is: ", s

print "The new sentence is: ", ans
