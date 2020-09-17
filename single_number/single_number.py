'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    arr = sorted(arr)
    i = 0
    j = 1
    while j < len(arr):
        if arr[i] != arr[j]:
            return arr[i]
        i += 2
        j += 2
    # base case largest number IS the only one of it's kind
    return arr[len(arr) - 1]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
