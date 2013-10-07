def contains(value, lst):
    """ (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """

    found = False

#pass#    for i in range(len(lst)):
##       for j in range(len(lst[i])):
##            if lst[i][j] == value:
##                found = True

#pass#    for sublist in lst:
##        if value in sublist:
##            found = True
        
#fail#    for item in lst:
##        if value == item:
##            value = True
    
#fail#    for i in range(len(lst)):
##        for j in range(len(lst[i])):
##            found = (lst[i][j] == value)
            
    return found

if __name__ == '__main__':
    import doctest
    doctest.testmod()

