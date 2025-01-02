class Solution:
    def addTwoNumbers(self, l1, l2):
        first = ''.join(reversed(''.join(str(i) for i in l1)))
        second = ''.join(reversed(''.join(str(i) for i in l2)))
        return list(map(int, str((int(first)+int(second)))))[::-1]

obj = Solution()
print(obj.addTwoNumbers([1,2,3],[4,5,6]))
#321 + 654 = 975