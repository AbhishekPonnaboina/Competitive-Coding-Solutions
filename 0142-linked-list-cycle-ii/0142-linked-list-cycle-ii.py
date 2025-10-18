# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                #i wrote the proof in the book you can check it there
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

        # so this is O(n) memory bro
        # if not head:
        #     return 


        # myhash = dict()

        # slow = head
        # fast = head

        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow is fast:
        #         myhash[slow] = True
        #         slow = slow.next

        #         while slow is not fast:
        #             myhash[slow] = True
        #             slow = slow.next
                
        #         break

        
        # slow = head 

        # while slow:
        #     if slow in myhash:
        #         return slow
        #     slow = slow.next
    
        

                

            
        