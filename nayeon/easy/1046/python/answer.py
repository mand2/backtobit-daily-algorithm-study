class Solution:
    # 이거는 안됨 뭐지..?! [1,3] => 1 나오고 [3,1]=> 3 나옴. 값이 2어야함.
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     while len(stones) > 1:
    #         stones.sort(reverse=True)
    #         stones.append(stones[0] - stones[1])
    #         del stones[0]
    #         del stones[1]
    #     # return max(stones)
    #     return stones[0]
    # 3 1 -> 3 1 2 -> 2


    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]
# 3 1 -> 3 1 2 -> 2
