class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr, res):
            i, j, k = 0, 0, 0
            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]<right_arr[j]:
                    res[k] = left_arr[i]
                    i+=1
                else:
                    res[k] = right_arr[j]
                    j+=1
                k+=1
            res[k:] = left_arr[i:] if i<len(left_arr) else right_arr[j:]
        def merge_sort(nums):
            if len(nums) == 1: return
            mid = len(nums)//2
            left_arr = nums[:mid]
            right_arr = nums[mid:]
            merge_sort(left_arr)
            merge_sort(right_arr)
            merge(left_arr, right_arr, nums)
        merge_sort(nums)
        return nums