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

#print(re.findall(r'''
#    \b[-\w]+, #find a word boundary, 1+ hypens or characters and a coma
#    \s     #find one whitespace
#    [-\w ]+  # 1+ hyphens and chars and explit spaces
#    [^\t\n] #ignore tabs and newlines
#
#
#''', data, re.X))

#using groups '( )'
#line = re.search(r'''
#    ^(?P<name>[-\w ]*,\s[-\w ]+)\t    #Last and first names, corrot means the beginning of the string
#    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t    # Email
#    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #Phone nr
#    (?P<job>[\w\s]+,\s[\w\s.]+)\t?    #job and company
#    (?P<twitter>@[\w\d]+)?$ #twitter, dollar sign marks the end of the string
#    
#''', data, re.X|re.MULTILINE) #multiline treats each line as the end of the string
#
#print(line)
#print(line.groupdict())


#using compile
line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t    #Last and first names, corrot means the beginning of the string
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t    # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #Phone nr
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?    #job and company
    (?P<twitter>@[\w\d]+)?$ #twitter, dollar sign marks the end of the string
    
''', re.X|re.M) 


#print(line.search(data).groupdict()) #prints only one line
for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))












