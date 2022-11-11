# -*- coding: utf-8 -*-

import collections

class Stack:
    
    def __init__(self):
        self.container = collections.deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def top(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container) == 0 
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return str(self.container)

