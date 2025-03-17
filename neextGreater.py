


def next_greater_elem(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]

        stack.append(i)

    return result

nums = [4, 5, 2, 10, 8]
print(next_greater_elem(nums))