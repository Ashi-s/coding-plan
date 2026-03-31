# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
           
        if not head or not head.next:
            return

        slow = head
        fast = head

        # reach center
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # split both and mark first have to end
        curr = slow.next # seconf half
        slow.next = None
        
        prev = None
        # reverse
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


        # After reverse prev will be at end
        node = head

        while prev:
            tmp1 = node.next
            tmp2 = prev.next

            node.next = prev
            node = tmp1

            prev.next = node
            prev = tmp2
        
        # return head



        
        