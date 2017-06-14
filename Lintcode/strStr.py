'''
@Copyright:LintCode
@Author:   cindy huang
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@DateTime: 2017.06.09
'''

class Solution:
    def strStr(self, source, target):
        # write your code here
        
        if target is None or source is None:
            return -1
            
        if len(target) == 0:
            return 0
            
        for i in xrange(len(source) - len(target)+1):
            for j in xrange(len(target)):
                if source[i+j] != target[j]:
                    break;
                    
            if j == len(target) - 1 and source[i+j] == target[j]:
                return i
                
        return -1
        
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:  # no break
                return i
        return -1
