class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0

        # 순서대로 정렬
        g.sort()
        s.sort()

        i = j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count+=1
                i+=1
            j+=1
        return count


    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     count = 0
    #     while min(g, s):
    #         if(min(g) <= min(s)):
    #             count += 1
    #             g.remove(min(g))
    #             s.remove(min(s))
    #         else:
    #             s.remove(min(s))
    #     return count
