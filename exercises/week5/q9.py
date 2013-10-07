def cap_song_repetition1(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    >>> cap_song_repetition1(['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola'], 'Lola')
    ['Venus', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))
    return playlist

def cap_song_repetition2(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    >>> cap_song_repetition2(['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola'], 'Lola')
    ['Venus', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) > 3:
        playlist.pop(song)
    return playlist

def cap_song_repetition3(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    >>> cap_song_repetition3(['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola'], 'Lola')
    ['Venus', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))
    return playlist

def cap_song_repetition4(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    >>> cap_song_repetition4(['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola'], 'Lola')
    ['Venus', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) > 3:
        playlist.remove(song)
    return playlist

if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
