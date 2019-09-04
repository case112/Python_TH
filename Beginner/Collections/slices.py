#Let's get in some slice practice!

#Create a new variable named slice1 that has the second, third, and fourth items from favorite_things.

#OK, let's do another test. Get the last two items from favorite_things and put them into slice2.

favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']

slice1 = favorite_things[1:4]

#OK, let's do another test. Get the last two items from favorite_things and put them into slice2.


slice2 = favorite_things[5:]

#Make a copy of favorite_things and name it sorted_things.

#Then use .sort() to sort sorted_things.

sorted_things = favorite_things[:]

sorted_things.sort()

#turn list backwards

sorted_things[::-1]


