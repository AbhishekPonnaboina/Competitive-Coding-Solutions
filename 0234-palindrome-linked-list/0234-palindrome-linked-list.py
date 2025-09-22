



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        # print(stack)

        while curr:
            if stack.pop() != curr.val:
                return False
            curr = curr.next
        
        return True


