
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        prev=dummy
        curr1=list1
        curr2=list2

        while curr1 and curr2 : 
            if curr1.val>curr2.val:
                prev.next=curr2
                prev=prev.next
                curr2=curr2.next
            else :
                prev.next=curr1
                prev=prev.next
                curr1=curr1.next
        while curr1 : 
            prev.next=curr1
            prev=prev.next
            curr1=curr1.next
        while curr2 : 
            prev.next=curr2
            prev=prev.next
            curr2=curr2.next
        return dummy.next