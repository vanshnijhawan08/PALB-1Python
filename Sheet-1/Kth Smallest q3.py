class Solution:
    def kthSmallest(self, arr, k):
        # sort the array
        arr.sort()
        
        # return kth smallest element
        return arr[k - 1]
