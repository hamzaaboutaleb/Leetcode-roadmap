class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        head = reverse(head)

        i = 0
        curr = head
        prev = head

        # Special case: removing the first node
        if n == 0:
            return reverse(head.next)

        while i <= n and curr:
            if i == n:
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
            i += 1

        return reverse(head)