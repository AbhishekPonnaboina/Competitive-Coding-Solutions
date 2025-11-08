#User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head1, head2 (heads of both the lists)
	
	Return Type: Node # driver code will print the Node->data
'''
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find intersection point in Y shaped Linked Lists.
class Solution:
    def intersectPoint(self, headA, headB):
        # code here
        #done in leetcode
        #all three approaches
        #proof in the book
        #this is the most optimal approach
        if not headA or not headB:return None

        curr1 = headA
        curr2 = headB
        

        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next

            if curr1 == curr2:
                return curr1
            
            if not curr1:
                curr1 = headB
            if not curr2:
                curr2 = headA
                
        return curr1