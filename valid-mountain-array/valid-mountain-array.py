class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) <= 2:
            return False
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                if i==1:
                    return False
                break
            
        for j in range(i,len(arr)):
            if arr[j] >= arr[j-1]:
                return False
        return True 
            
        