

def minMax(nums):
    if len(nums) == 0:
        print("Empty list")
        return
    
    if len(nums) == 1:
        print(f"Min1 = Max1 = {nums[0]}")
        return
    
    min1, min2 = float('inf'), float('inf')
    max1, max2 = -float('inf'), -float('inf')

    for nr in nums:
        if min1 > nr:
            min1, min2 = nr, min1
        elif min2 > nr:
            min2 = nr

        if max1 < nr:
            max1, max2 = nr, max1
        elif max2 < nr:
            max2 = nr

    print(min1, min2, max1, max2)

minMax([1,2])