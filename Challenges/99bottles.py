numofbottles = 99
while numofbottles >= 1:
    if numofbottles == 1: # Last line of the song
        print str(numofbottles) + " bottle of beer on the wall, "
        print str(numofbottles) + " bottle of beer."
        print "Take one down and pass it around..."
        print "No more bottles of beer on the wall."
        print "No more bottles of beer on the wall,"
        print "No more bottles of beer."
        print "Go to the store and buy some more,"
        print "99 bottles of beer on the wall."
        numofbottles = numofbottles - 1
    else: # Every other line
        print str(numofbottles) + " bottles of beer on the wall, "
        print str(numofbottles) + " bottles of beer."
        print "Take one down and pass it around..."
        numofbottles = numofbottles - 1
