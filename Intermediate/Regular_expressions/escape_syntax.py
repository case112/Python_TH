#    \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", 
#    \w would  match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
#    \W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
#    \s - matches whitespace, so spaces, tabs, newlines, etc.
#    \S - matches everything that isn't whitespace.
#    \d - is how we match any number from 0 to 9
#    \D - matches anything that isn't a number.
#    \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
#    \B - matches anything that isn't the edges of a word.

#    Two other escape characters that we didn't cover in the video are \A and \Z. These match the beginning and the end of the string, respectively. 
#    As we'll learn later, though, ^ and $ are more commonly used and usually what you actually want.


#    \w{3} - matches any three word characters in a row.
#    \w{,3} - matches 0, 1, 2, or 3 word characters in a row.
#    \w{3,} - matches 3 or more word characters in a row. There's no upper limit.
#    \w{3, 5} - matches 3, 4, or 5 word characters in a row.
#    \w? - matches 0 or 1 word characters.
#    \w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
#    \w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
#    .findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.


##SETS

#    [abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
#    [a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
#    [0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.


#    [^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.
#    re.IGNORECASE or re.I - flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.
#    re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.


#    ([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
#    (?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. 
#    This could later be accessed from the Match object as .group('name').
#    .groups() - method to show all of the groups on a Match object.
#    re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.
#    ^ - specifies, in a pattern, the beginning of the string.
#    $ - specifies, in a pattern, the end of the string.

###COMPILING AND LOOPS


#    re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
#    .groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. 
#    The values will be the results of the patterns in the group.
#    re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
#    .group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many 
#    groups you have will get that group. Or use a group's name to get it if you're using named groups.

