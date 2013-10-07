def get_length(dna): ### SUCCESS ###
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT') #works
    6
    >>> get_length('ATCG') #works
    4
    """
    return len(dna) 

def is_longer(dna1, dna2): ### SUCCESS ###
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT') #works
    True
    >>> is_longer('ATCG', 'ATCGGA') #works
    False
    """
    return len(dna1)>len(dna2) 


def count_nucleotides(dna, nucleotide): ### SUCCESS ###
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G') #works
    2
    >>> count_nucleotides('ATCTA', 'G') #works
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2): ### SUCCESS ###
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.find(dna2)!=-1


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if the number of violators in the string dna is zero, false 

    >>> is_valid_sequence('ACTG') #works
    True
    >>> is_valid_sequence('ACBTG') #works
    False
    >>> is_valid_sequence('') #works
    True
    """

    nucleotides=0

    for nucleotide in dna:
        if nucleotide in 'ACTG':
            nucleotides = nucleotides + 1
            
    return len(dna)==0 or (nucleotides - len(dna)) == 0


def insert_psequence(dna1, dna2, index): 
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second
    DNA sequence dna2 into the first DNA sequence dna1 at the given index index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'

    also test end cases for insertion at zero, end, and past either

      
    """

    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """

    complement = ''
    
    if nucleotide == 'A':
        complement =  'T'
    elif nucleotide == 'T':
        complement = 'A'
    elif nucleotide == 'C':
        complement =  'G'
    elif nucleotide == 'G':
        complement = 'C'

    return complement

def get_complementary_sequence(dna):
    """ (str) -> str

    Takes string dna and returns complement string

    >>> get_complementary_sequence('ACTG')
    'TGAC'

    for A in dna swap them and move to next
    """

    complement = ''

    for nucleotide in dna:
        complement = complement + get_complement(nucleotide)
    return complement

''' old version i am replacing with code re-use
    for nucleotide in dna:
        if nucleotide == 'A':
            complement = complement + 'T'
        elif nucleotide == 'T':
            complement = complement + 'A'
        elif nucleotide == 'C':
            complement = complement + 'G'
        elif nucleotide == 'G':
            complement = complement + 'C'
    return complement
'''


