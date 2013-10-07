def shift_left(L):
    ''' (list) -> NoneType

      Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    '''
    
    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item


def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1
    '''
    
##  correct_right: ['0','1','2','3'] -> ['3', '0', '1', '2']
    
    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]        
        
    L[0] = last_item # this is working, the last item is set properly
    

