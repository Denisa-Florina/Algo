def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1  
        else:
            left = mid + 1  

    return -1  


def binary_search_recursive(nums, left, right, target):
    if left > right:
        return -1 

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search_recursive(nums, left, mid - 1, target)
    else:
        return binary_search_recursive(nums, mid + 1, right, target)



nums = [-5, -2, 0, 3, 8, 12, 17]
target = 8

index = binary_search(nums, target)
print(f"Target found at index: {index}" if index != -1 else "Target not found!")