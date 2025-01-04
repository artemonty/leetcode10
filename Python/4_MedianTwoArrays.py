class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new_nums = []
        for num in nums1:
            new_nums.append(num)
        for num in nums2:
            new_nums.append(num)
        new_nums.sort()
        if len(new_nums) % 2 == 0:
            return (new_nums[len(new_nums) // 2 - 1] + new_nums[len(new_nums) // 2]) / 2.0
        else:
            return new_nums[len(new_nums) // 2]

obj = Solution()
print(obj.findMedianSortedArrays([1,2], [3,4]))