# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head):
            curr=head
            length=0
            while curr : 
                length+=1 
                curr=curr.next
            return length
        
        length1=get_length(headA)
        length2=get_length(headB)
        curr1=headA
        curr2=headB
        if length1>length2 : 
            while length1!=length2:
                curr1=curr1.next
                length1-=1

        elif length1<length2:
            while length1!=length2:
                curr2=curr2.next
                length2-=1
        
        while curr1 : 
            if curr1==curr2 : 
                return curr1 
            curr1=curr1.next
            curr2=curr2.next