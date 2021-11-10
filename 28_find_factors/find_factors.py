def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    temp_set = set()
    for i in range(1,num+1):
        if num % i==0:
            temp_set.add(i)
    
    solution = list(temp_set)
    solution.sort()
    return solution


