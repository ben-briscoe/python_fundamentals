def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)
    temp_dict_1 = dict()
    for digit in num1:
        if digit in temp_dict_1.keys():
            temp_dict_1[digit] += 1
        else:
            temp_dict_1[digit] = 1
    
    temp_dict_2 = dict()
    for digit in num2:
        if digit in temp_dict_2.keys():
            temp_dict_2[digit] += 1
        else:
            temp_dict_2[digit] = 1

    if temp_dict_1==temp_dict_2:
        return True
    else:
        return False