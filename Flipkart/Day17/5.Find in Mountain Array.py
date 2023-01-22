class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        index = self.binary_search(mountain_arr, 0, peak, target, True)
        if index != -1:
            return index
        return self.binary_search(mountain_arr, peak + 1, n - 1, target, False)
    
    def binary_search(self, mountain_arr, l, r, target, is_ascending):
        while l <= r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) == target:
                return mid
            if is_ascending:
                if mountain_arr.get(mid) < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if mountain_arr.get(mid) > target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1