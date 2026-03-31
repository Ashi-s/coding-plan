# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = ListNode()
        curr = head
        dummy.next = head

        node = head

        while n > 0:
            curr = curr.next
            n -= 1
        
        while curr:
            prev = node
            node = node.next
            curr = curr.next
        
        prev.next = node.next

        return dummy.next

        
        

