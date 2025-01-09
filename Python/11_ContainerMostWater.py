class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area
            width = right - left
            current_area = width * min(height[left], height[right])
            max_area = max(max_area, current_area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
obl = Solution()
print(obl.maxArea([1,8,6,2,5,4,8,3,7]))