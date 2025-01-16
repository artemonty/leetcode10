class Solution(object):
    def romanToInt(self, s):
        keys = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)-1):
            if keys[s[i]] < keys[s[i+1]]:
                total -= keys[s[i]]
            else:
                total += keys[s[i]]
        total += keys[s[-1]]
        return total
obl = Solution()
print(obl.romanToInt("MCMXCIV"))