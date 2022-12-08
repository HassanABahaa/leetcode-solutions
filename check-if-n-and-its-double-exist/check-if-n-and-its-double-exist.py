class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)): 
                if arr[i] == arr[j]*2 and i!=j:
                    return True
            