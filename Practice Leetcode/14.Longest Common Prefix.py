# -*- coding: utf-8 -*-

class Solution:
    def longestCommonPrefix(self, strs):
        
        shortestWord = [0, len(strs[0])]
                        
        for i in range(len(strs)):
            if len(strs[i]) < shortestWord[1]:
                shortestWord = [i, len(strs[i])]
        res = ""
        for j in range(shortestWord[1]):
            count = 0 
            for k in range(len(strs)):
                if strs[k][j] == strs[0][j]:
                    count += 1       
            if count == len(strs):
                res += strs[k][j]
            else:
                break
        return res

solu = Solution()
strs = ["flower","flow","flight"]
res = solu.longestCommonPrefix(strs)
print("res1",res)
