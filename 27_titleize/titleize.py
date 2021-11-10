def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    letters = 'abcdefghijklmnopqrstuv'
    in_word = False
    solution = ''
    for letter in phrase:
        if in_word == False and letter in letters:
            solution+= letter.upper()
            in_word = True
        elif in_word == True and letter == ' ':
            in_word = False
            solution+= letter
        else:
            solution+= letter
    
    return solution
