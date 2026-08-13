# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(second):
            prev=None
            curr=second 
            while curr :
                next=curr.next 
                curr.next=prev  
                prev=curr
                curr=next
            return prev
        slow=head 
        fast = head 
        while fast and fast.next : 
            fast=fast.next.next
            slow=slow.next
        slow=reverseList(slow)
        curr=head
        while slow:
            if slow.val!=curr.val:
                return False 
            slow=slow.next
            curr=curr.next
        return True

        