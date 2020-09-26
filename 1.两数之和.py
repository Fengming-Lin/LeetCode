"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


class Solution(object):

    # 两层循环暴力解法
    def twoSum_1(self, nums, target):
        res = []
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res

    # Hash 字典
    def twoSum_2(self, nums, target):
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = i
            if dict1.get(target - nums[i]) is not None:
                return [dict1.get(target - nums[i]), dict1.get(nums[i])]


if __name__ == '__main__':
    a = [2, 7, 11, 15]
    b = 9
    output = Solution.twoSum_2(Solution, a, b)
    print(output)





