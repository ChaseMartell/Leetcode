#Returns in the indices in an array that add up to the target number, else returns empty array.
def twoSum(nums, target):
    hash_map = {}

    for i, number in enumerate(nums):
        complement = target - number
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[number] = i
    return []

def main():
    test_array1 = [0,1,2,3,4,5,6,7,8,9,10]
    test_array2 = [1034,53905,6854698,498,349898,344,3813]

    print(twoSum(test_array1, 5))
    print(twoSum(test_array2, 4847))
    print(twoSum(test_array2, 5545455))

if __name__ == "__main__":
    main()


