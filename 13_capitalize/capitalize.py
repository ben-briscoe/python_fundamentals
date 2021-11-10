def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    found_it = False
    check ='abcdefghijklmnopqrstuvwxyz'
    new_phrase = ""
    for letter in phrase:
        if found_it==False:
            if check.count(letter.lower())!=0:
                found_it = True
                new_phrase += letter.upper()
            else:
                new_phrase+= letter
        else:
            new_phrase+= letter
                
    return new_phrase
    