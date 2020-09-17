'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    window = [0 for i in range(k)]
    output = []
    for i in range((len(nums) - k + 1)):
        m = i
        j = 0
        while j < len(window):
            while m < (i + len(window)):
                print(j)
                window[j] = nums[m]
                m += 1
                j += 1
        output.append(max(window))
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
