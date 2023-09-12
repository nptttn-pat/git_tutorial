def find_three_numbers(nums):
    n = len(nums)
    result = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([i, j, k])

    return result

try:
    input_str = input("Input: ")
    nums = [int(num) for num in input_str.strip('[]').split(',')]
    
    if len(nums) < 3:
        print("Please provide at least three numbers in the input list.")
    else:
        indices = find_three_numbers(nums)

        if not indices:
            print("Can’t find")
        else:
            
            for idx in indices:
                print(idx)

except ValueError:
    print("Invalid input. Please enter numbers separated by commas inside square brackets.")
