# -*- coding: utf-8 -*-
class Solution:
    global n
    n = 0 
    def removeDuplicates(self, nums):
        dic = {}
        res = []
        for i in range(len(nums)):
            dic[nums[i]] = 0
              
        for k in dic.keys():
            res.append(k)
        nums = res
        return [len(res), nums]

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))