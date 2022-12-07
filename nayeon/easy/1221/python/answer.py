class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) is 2: return 2

        result = 0
        cnt = 0
        for l in s:
            cnt += 1 if l is 'L' else -1
            if cnt == 0: result += 1

        return result
