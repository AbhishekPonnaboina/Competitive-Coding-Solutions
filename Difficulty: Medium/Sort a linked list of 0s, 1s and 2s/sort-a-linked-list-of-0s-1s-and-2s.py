'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        if not head:
            return
        zero = Node(9)
        one = Node(9)
        two = Node(9)
        
        z = zero
        o = one
        t = two

        
        curr = head
        
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
            
        if o.next:
            zero.next = o.next
        else:
            zero.next = t.next
        one.next = t.next
        two.next = None
        
        return z.next

            
        
        
        #basic approach
        # if not head:
        #     return 
        # zero = 0
        # one = 0
        # two = 0
        
        
        # curr = head
        
        # while curr:
        #     if curr.data == 1:
        #         one += 1
        #     elif curr.data == 2:
        #         two += 1
        #     else:
        #         zero += 1
        
        # curr = head
        
        # while curr:
        #     if zero:
        #         curr.data = 0
        #         zero -= 1
        #     elif one:
        #         curr.data = 1
        #         one -= 1
        #     else:
        #         curr.data = 2
        #         two -= 1
        #     curr = curr.next
        
        # return head
        
        
        
        
        
        
        
        
        
        
    