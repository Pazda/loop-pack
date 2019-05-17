# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:27:33 2019

@author: Tim
"""

MAX_ITEMS = 20 #This code operates (at first glance, at least) at O(2^n). Increasing this may drastically increase processing time.
OUTPUT_FILE = "d:\\packages.txt" #Where you would like this to output to

#Don't touch anything below here unless you know what you're doing! :)
#File stuff
fout = open( OUTPUT_FILE, "w" )
fout.truncate(0)

maximum = 2870

items = {
    "Aluminum Bottle": 60,
    "Small Tiffin": 86,
    "Medium Tiffin": 111,
    "Large Tiffin": 182,
    "Jar": 80,
    "Vinegar and Oil": 67,
    "Body Shop Tea Tree": 31,
    "Clorox": 171
}

#Clean binary number creator
def myBin( a ):
    return format(a, "0" + str(len(items)) + "b")

for i in range( 2**len(items) ):
    working = []
    for j in range( len(items) ):
        if str( myBin( i ) )[len(items)-j-1] == '1':
            working.append( list(items.keys())[j] )
    
    weight = sum( [items[k] for k in working] )
    if weight < maximum:
        fout.write(str(working) + " :: " + str(weight) + "in.\n")
        
fout.close()