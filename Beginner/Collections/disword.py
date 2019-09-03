def disemvowel(word):
    vowels =['a','e','i','o', 'u']
    new_word = ""
    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter
    return new_word

print(disemvowel("dflkjhsaaawawaaeioiaoaoeiaoeiaej"))