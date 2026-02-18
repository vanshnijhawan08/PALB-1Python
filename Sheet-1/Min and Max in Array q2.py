class Solution:
    def getMinMax(self, arr):
        # assume first element is both min and max
        minimum = arr[0]
        maximum = arr[0]
        
        # check remaining elements
        for i in range(1, len(arr)):
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i] > maximum:
                maximum = arr[i]
        
        return [minimum, maximum]
