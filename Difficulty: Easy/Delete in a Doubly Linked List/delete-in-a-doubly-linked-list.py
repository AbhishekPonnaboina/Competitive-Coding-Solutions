class Solution:
    def delete_node(self, head, pos):
        #code here
        if head is None:
            return None
        if pos == 1:
            next_node = head.next
            if next_node:
                next_node.prev = None 
            return next_node
        curr = head
        for _ in range(pos-2):
            curr = curr.next
            if curr is None:
                return head
                
                
        nodetodelete = curr.next
        if nodetodelete is None:
            return head
        nextnode = nodetodelete.next
        curr.next = nextnode
        if nextnode:
            nextnode.prev = curr
        return head
        
        
        
        
        
        
        
        
        
        
        return head
        



