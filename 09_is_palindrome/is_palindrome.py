def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    is_palindrome = True
    if len(phrase)%2==0:
        reverse_index=len(phrase)
        index = -1
        while index < (len(phrase)/2):
            index += 1
            reverse_index -= 1
            if phrase[index]!=phrase[reverse_index]:
                is_palindrome=False
    else:
        reverse_index=len(phrase)
        index = -1
        while index < (len(phrase)/2)-0.5:
            index += 1
            reverse_index -= 1
            if phrase[index]!=phrase[reverse_index]:
                is_palindrome=False

    if is_palindrome==True:
        return True
    else:
        return False