class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head: return []
        res, stack = [], []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            res.append(stack.pop())
        return res
