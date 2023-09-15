def find_three_numbers(nums):
    n = len(nums)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    return [i, j, k]

    return "Can't find"

# Test case 1
input1 = [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
output1 = find_three_numbers(input1)
print("Input: ", input1)
print("Test case 1:", output1)

# Test case 2
input2 = [1, 2, 3, 4, 5]
output2 = find_three_numbers(input2)
print("Input: ",input2)
print("Test case 2:", output2)
