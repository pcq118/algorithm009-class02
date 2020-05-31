class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1.暴力：两个循环 n^2 
        #2.dic 存值 (n)
        dic={}
        for i, n in enumerate(nums):
            if target - n in dic:
                return [dic[target-n],i]
            dic[n]=i