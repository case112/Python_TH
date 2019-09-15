import re


names_file = open('names.txt', encoding = 'utf-8')
data = names_file.read()
names_file.close()

#print(re.match(r'Love', data))
#rint(re.search(r'Kenneth', data))

#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

#print(re.findall(r'\w*, \w+', data))

#email
#print(re.findall(r'[-\w\d+.]+@[-\w\d+.]+', data))

#treehouse
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))

#print(re.findall(r'''
#
#    \b@[-\w\d+.]* #First a word boundry, an @, then any num of chars
#   [^gov\t]+ #ignore one or more instances of the letters 'g' 'o' or 'v' and a tab
#    \b #match annother word boundary
#
#''', data, re.VERBOSE|re.I))

print(re.findall(r'''
    \b[-\w]+, #find a word boundary, 1+ hypens or characters and a coma
    \s     #find one whitespace
    [-\w ]+  # 1+ hyphens and chars and explit spaces
    [^\t\n] #ignore tabs and newlines


''', data, re.X))