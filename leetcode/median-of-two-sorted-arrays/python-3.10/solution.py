class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if len(nums) % 2 == 0:
            return (nums[length // 2] + nums[length // 2 - 1]) / 2
        return nums[length // 2]
