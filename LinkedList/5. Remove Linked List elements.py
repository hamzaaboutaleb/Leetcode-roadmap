
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev=dummy
        curr=head 
        while curr : 
            if curr.val!=val : 
                prev.next=curr
                prev=prev.next
            curr=curr.next
        prev.next=None
        return dummy.next