class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        m = int(size / 2)
        r = size
        l = 0
        while l < r :
            m = int((r + l) / 2)
            if nums[m] == target: 
                return m
            if  target < nums[m]:
                r = m-1         
            if target > nums[m]:
                l = m + 1

        return -1
