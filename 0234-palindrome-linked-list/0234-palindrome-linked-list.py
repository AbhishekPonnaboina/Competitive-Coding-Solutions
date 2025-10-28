class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head

        for i,val in enumerate(reversed(stack)):
            if val != curr.val:
                return False
            curr = curr.next
        return True