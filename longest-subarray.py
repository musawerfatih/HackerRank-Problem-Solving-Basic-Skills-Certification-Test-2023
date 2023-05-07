def longestSubarray(arr):
    n = len(arr)
    if n <= 2:
        return n

    left, right = 0, 1
    max_length = 0

    while right < n:
        if len(set(arr[left:right+1])) <= 2 and abs(arr[right] - arr[left]) <= 1:
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            left += 1

    return max_length
