class Solution:
    def reverse(self, x):
        znak = -1 if x < 0 else 1
        a = int(str(abs(x))[::-1]) * znak
        if -2 ** 31 <= a <= 2 ** 31 - 1:
            return a
        else:
            return 0

obj = Solution()
print(obj.reverse(123))