class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        n = len(arr)
        i = 0
        
        while i < n - 2:
            left = i + 1
            right = n - 1
            
            while left < right:
                s = arr[i] + arr[left] + arr[right]
                
                if s == target:
                    return True
                elif s < target:
                    left += 1
                else:
                    right -= 1
            
            i += 1
        
        return False
