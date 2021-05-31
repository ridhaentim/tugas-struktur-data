# C-1.25
#WriteashortPython function thattakes astrings,representing asentence,
#and returns a copy of the string with all punctuation removed. For example,
#if given the string "Let s try, Mike.", this function would return "Lets try Mike".
#
given_string = 'Let\'s try, Mike.'

punctuations = ''''~!@#$%^*()_-{}[]|\:'";<>,./'''  # Take help of your keyboard to remember this.

newstring = ''
for i in given_string:
    if i not in punctuations:
        newstring += i

print(newstring)
