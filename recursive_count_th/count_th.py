'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    if len(word) == 0:
        return 0
    if word[0:2] == "th":
        return count_th(word[1:]) +1
    return count_th(word[1:])

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
