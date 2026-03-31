# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # center to divide in two
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is center
        second = slow.next
        slow.next = None # seperate them

        # rever the second LL
        prev = None
        curr = second

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # prev becomes the start of reverse pointer
        # head is start of first LL & prev start of second LL

        node = head

        while prev:
            tmp1 = node.next
            tmp2 = prev.next

            node.next = prev
            node = tmp1

            prev.next = node 
            prev = tmp2
            