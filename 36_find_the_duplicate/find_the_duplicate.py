def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    inner_index = 0
    for i in range(len(nums)):
        inner_index+=1
        inner_index= inner_index-1 if inner_index>len(nums) else inner_index
        for j in range(inner_index,len(nums)):
            if nums[i]==nums[j] and i!=j:
                return nums[i]
    
    return None