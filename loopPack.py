"""
Created on Mon Jan  7 18:56:38 2019
Loop shipping container combination generator
Created for Terracycle/Loop
@author: Tim Swyzen
@email: tswyoff42@gmail.com
Please contact me for any questions via email.
"""
#For user to edit!!!!!
MAX_ITEMS = 20 #This code operates (at first glance, at least) at O(2^n). Increasing this may drastically increase processing time.
OUTPUT_FILE = "d:\\packages.txt" #Where you would like this to output to

#Don't touch anything below here unless you know what you're doing! :)
#File stuff
fout = open( OUTPUT_FILE, "w" )
newF = open( OUTPUT_FILE, "r" )
fout.truncate(0)

"""Set up data
I added small prime decimals to each piece of data so that coincidences would not disallow some combinations.
I checked for duplicates just by checking against a list of all previously processed sums. Having the primes
and then rounding them makes sure coincidences are rare, although they may still occur.
Alternatives were not viable as far as I could tell, but I may be mistaken.
"""
fNumbers = [ 60.001, 86.003, 111.005, 182.007, 80.011, 67.013, 31.017, 171.002 ]
maximum = 2580.75
sums = []

#Start recursion
def my_sum( numbers, target, count, partial=[] ):
    #TRIPLE CHECK that if it's above target, we escape. Just for safety. 
    global sums
    if sum(partial) > target:
        return
    
    #Stop early if we want to save processing time.
    if count > MAX_ITEMS:
        return
    count = count + 1
    
    #Just writing stuff to the file.
    fout.write( "[ " )
    for i in range( len( partial )  ):
        if partial[i] == 60.001:
            fout.write( "Aluminum Bottle (60 in), " )
        elif partial[i] == 86.003:
            fout.write( "Small Tiffin (86 in), " )
        elif partial[i] == 111.005:
            fout.write( "Medium Tiffin (111 in), " )
        elif partial[i] == 182.007:
            fout.write( "Large Tiffin (182 in), " )
        elif partial[i] == 80.011:
            fout.write( "Jar (80 in), " )
        elif partial[i] == 67.013:
            fout.write( "Vinegar and Oil (67 in ), " )
        elif partial[i] == 31.017:
            fout.write( "Body Shop Tea Tree (31 in), " )
        elif partial[i] == 171.002:
            fout.write( "Clorox (171 in), " )
    fout.write( " ] = %s\n" % round( sum(partial), 3 ) )
        
    #Update our sums list so we don't have duplicates.
    sums = sums + [ round( sum(partial), 3 ) ]
           
    #Fancy iteration... I hope
    for i in range( len(numbers) ):
        n = numbers[i]
        newSum = round( sum( partial ) + n, 3 )
        if newSum <= target:
            if newSum not in sums:
                my_sum( numbers, target, count, partial + [n] )
            else:
                continue

        else:
            return
            
my_sum( fNumbers, maximum, 0 )

fout.close()
newF.close()
