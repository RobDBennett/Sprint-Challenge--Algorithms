'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, count=0):
    if len(word) < 2: #Checks if word is less than the size of th. If so, a th can't physically be present, return the current count.
        return count
    if word[:2] == "th": #Slice the word up, check if 0 and 1 are th.
        count += 1 #Increase count if true.
        return count_th(word[2:], count) #Use recursion. Eliminate those values and check again (since if th is present, the next value cannot also be th)
    else:
        return count_th(word[1:], count) #Otherwise take off 1 letter and use recursion to check again.

"""
Too many pointers. Lets try another way.
def count_th(word, count=0, track=0):
    if track > len(word):
        return count
    if word[track] and word[track+1] == "th":
        count += 1
        track += 1
        return count_th(word, count, track)
    else:
        track += 1
        return count_th(word, count, track)
"""
"""
def count_th(word):
    #This absolutely works, but the requirements for the challenge
    # is to utilize recursion, so lets try another method.    
    x = word.count("th")
    return x
"""
