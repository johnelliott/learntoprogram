def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE MISSING HERE
#fail#    for s in sentences:
##        file.write(s)
##    file.write('\n')
    
    for s in sentences:
        file.write(s)
        file.write('\n')

#pass#    for s in sentences:
##        file.write(s + '\n')

#fail#    file.write(sentences)

#fail#    for s in sentences:
##        file.write(s)
