# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:00:03 2022

@author: berni
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            '(':')',
            '[':']',
            '{':'}'            
        }
        
        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or stack[-1]!=char:
                return False
            else:
                stack.pop()
        
        return len(stack)==0
    
sol = Solution()

print(sol.isValid("[]{}()"))