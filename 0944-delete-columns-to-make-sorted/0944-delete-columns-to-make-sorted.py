class Solution(object):
    def minDeletionSize(self, strs):
        x = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j-1][i] > strs[j][i]:
                    x += 1
                    break
        
        return x