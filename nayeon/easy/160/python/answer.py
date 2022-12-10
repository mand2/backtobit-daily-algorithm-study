# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 파이썬은 linkedlist 도 set 으로 만들 수 있을줄 알았는데 iterable 아니면 set 쓸 수 없음.
        # c = set(headA)&set(headB)

        """
        IDEAS FROM
        https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/1092898/js-python-java-c-easy-o-1-extra-space-solution-w-visual-explanation/
        """

        pointA = headA
        pointB = headB

        while pointA != pointB:

            pointA = headB if pointA is None else pointA.next
            pointB = headA if pointB is None else pointB.next

        return pointA

