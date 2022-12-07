class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] in nums[i+1:]:
                nums.remove(nums[i])
            else:
                i+=1
    