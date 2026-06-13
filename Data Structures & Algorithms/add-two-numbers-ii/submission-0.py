# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        curr = head

        prev = None
        while curr:
            nexxt = curr.next
            curr.next = prev
            prev = curr
            curr = nexxt
        
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        head = dummy = ListNode()

        carry = 0
        
        while l1 or l2 or carry:
            add = 0
            if l1:
                add += l1.val
                l1 = l1.next
            
            if l2:
                add += l2.val
                l2 = l2.next
            
            add += carry
            
            mod = add % 10
            carry = add // 10

            dummy.next = ListNode(mod)
            dummy = dummy.next
        
        return self.reverse(head.next)


