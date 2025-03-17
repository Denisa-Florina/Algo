def subarray_sum(arr, S):
    start = 0
    current_sum = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum > S and start < end:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == S:
            return arr[start:end+1]
    
    return None

arr = [1, 4, 20, 3, 10, 5]
S = 33
print(subarray_sum(arr, S))  