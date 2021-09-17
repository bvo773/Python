
def twoSum(numbers, target):
    result = []
    complementSet = {}
    for number in numbers:
        complement = target - number
        if (complement in complementSet):
            result[0] = complementSet[complement]
            result[1] = numbers.index(number)
            break
        complementSet[number] = numbers.index(number)
    return result


def main():
    nums = [2, 7, 11, 15]
    # nums = twoSum(nums, 9)
    hashMap = {}
    hashMap[2] = 1
    hashMap[3] = 2
    print (hashMap[3])
    print (nums.index(7))
if __name__ == '__main__':
    main()