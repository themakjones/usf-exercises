def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    curr_mode = 0
    high_count = 0

    for num in nums:
        if nums.count(num) > high_count:
            print(high_count)
            # high_count = nums.count(num)
            # curr_mode = num
    
    # return curr_mode

    print(mode([1,2,1]))
    print(mode([2,2,3,3,2]))
