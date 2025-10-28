class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #follow up is how can we do it without extra space?
        #finding the middle part
        #revrsing 
        #checking for the palindrom
        #before returning the ans we make sure to reverse what we changed
        def reversehelpie(head):
            prev = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = reversehelpie(slow.next)
        start = head

        while mid:
            if start.val != mid.val:
                reversehelpie(slow.next)
                return False
            start = start.next
            mid = mid.next
        else:
            reversehelpie(slow.next)
            return True
        

        #basic approach my nig
        # stack = []
        # curr = head

        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        
        # curr = head

        # for i,val in enumerate(reversed(stack)):
        #     if val != curr.val:
        #         return False
        #     curr = curr.next
        # return True