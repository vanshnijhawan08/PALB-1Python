class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        n1 = len(arr1)
        n2 = len(arr2)
        n3 = len(arr3)
        
        result = []
        
        while i < n1 and j < n2 and k < n3:
            if arr1[i] == arr2[j] == arr3[k]:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                minimum = min(arr1[i], arr2[j], arr3[k])
                
                if arr1[i] == minimum:
                    i += 1
                if arr2[j] == minimum:
                    j += 1
                if arr3[k] == minimum:
                    k += 1
        
        if not result:
            return [-1]
        
        return result
