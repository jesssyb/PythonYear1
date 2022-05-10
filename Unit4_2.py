#Song list
#Dec 16
#Jessica

#Input
song = ["Take Me to Church", "Believer", "ilomilo", "Green Light", "River"]
artist = ["Hozier", "Imagine Dragons", "Billie Eillish", "Lorde", "Bishop Briggs"]

s = raw_input("Enter your favorite song: ")

if s in song:
    print "We agree"
    print "There is a total of", len(song), "in the list"
else:
    print "I'll have to add that to my list"
    s2 = song.append(s)
    a = raw_input("Enter the artist name: ")
    a2 = artist.append(a)
    print "There is a total of", len(song), "in the list"
    
