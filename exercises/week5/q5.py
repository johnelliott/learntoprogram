def sum_odds(start,end):
    '''(int, int) -> int

    Return the sum of every other number from start to end, inclusive

    >>> sum_odds(1, 2)
    1
    >>> sum_odds(1, 3)
    4
    >>> sum_odds(1, 6)
    9
    '''
    i = 0
    total = 0
        
    for i in range(start, end+1, 2):
        total = total + i
    return total  


if __name__ == '__main__':
    import doctest
    doctest.testmod()
