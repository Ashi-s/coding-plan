# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = left
        r = right

        curr1 = head
        prev = None
        while l > 1:
            prev = curr1
            curr1 = curr1.next
            l -= 1
        
        curr2 = head
        while r > 1:
            curr2 = curr2.next
            r -= 1
        
        next_node = curr2.next
        curr2.next = None

        # reverse
        # curr1 is left and curr2 is right and curr2.next is already None
        prevv = None
        curr = curr1
        while curr:
            tmp = curr.next
            curr.next = prevv
            prevv = curr
            curr = tmp
        
        
        curr1.next = next_node
        if prev:
            prev.next = prevv
            return head
        else:
            return prevv