class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
       arr.sort()
       min_diff=float('inf')
       result = []

       for i in range(len(arr) - 1):
        diff = abs(arr[i+1] - arr[i])
        if diff < min_diff:
            min_diff = diff

       for i in range(len(arr) - 1):
        if abs(arr[i+1] - arr[i]) == min_diff:
            result.append([arr[i], arr[i+1]]) 
        
    
       return result