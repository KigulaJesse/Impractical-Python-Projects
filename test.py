""""""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            for other_num in nums:
                if num == other_num:
                    continue
                elif (num - other_num) == target:
                    return [nums.index(num),nums.index(other_num)]
answer = Solution()
values = answer.twoSum([2,7,11,15],9)
print(values)
