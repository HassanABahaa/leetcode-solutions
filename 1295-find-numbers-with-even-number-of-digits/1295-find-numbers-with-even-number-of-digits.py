class Solution(object):
    def findNumbers(self, nums):
        Even = 0
        for num in nums:
            count = 0
            while num != 0:
                count += 1
                num //= 10
            if count % 2 == 0:
                Even += 1
        return Even