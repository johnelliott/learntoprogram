def while_version(L):
    """ (list of number) -> number

    >>> while_version([1, 3, 2, 3])
    4
    """
    
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1
    return total


def for_version1(L):
    """ (list of number) -> number

    >>> for_version1([1, 3, 2, 3])
    4
    """ 
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

def for_version2(L):
    """ (list of number) -> number

    >>> for_version2([1, 3, 2, 3])
    4
    """ 

    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
            found_even = True

    return total

def for_version3(L):
    """ (list of number) -> number

    >>> for_version3([1, 3, 2, 3])
    4
    """ 
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total


def for_version4(L):
    """ (list of number) -> number

    >>> for_version4([1, 3, 2, 3])
    4
    """ 

    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total



if __name__ == '__main__':
    import doctest
    doctest.testmod()
