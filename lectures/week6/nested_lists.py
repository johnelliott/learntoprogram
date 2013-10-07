def calculate_averate(asn_grades):
    ''' (list of list of [str, number]) -> float

    Return the average of the grades in asn_grades.

    >>> calculate_averate([['A1', 80], ['A2', 90]])
    85.0
    '''

    total = 0

    for item in asn_grades:
        total = total + item [1]

    return total / len(asn_grades)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
