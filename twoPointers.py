
def twoPointers(nums, target):
    left = 0
    right = len(nums)-1

    while(left < right):
        nr1 = nums[left]
        nr2 = nums[right]
        sum = nr1 + nr2

        if sum == target:
            return left, right
        elif sum < target:
            left += 1
        else:
            right -= 1
        
    return -1, -1



def main():
    nums = [1, 2, 3, 6, 8, 11, 15]
    target = 9

    i1, i2 = twoPointers(nums, target)

    if(i1 == i2 == -1):
        print("IMPOSSIBLE")
    else:
        print(f"i1: {i1}, i2: {i2}")

main()