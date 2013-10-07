def mystery(s):
    """ (str) -> bool

    Returns True if and only if

    >>> mystery('civil')
    False

    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # check to see if the character at index i is equal to the character 
            matches = matches + 1   # increment matches
    
    return matches == (len(s) // 2) # is matches equal the length of half
                                    # of the string less a possible middle character?
