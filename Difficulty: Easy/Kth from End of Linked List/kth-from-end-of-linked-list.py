#User function Template for python3
'''
    A linked list node has the following structure
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        curr_node = head
        kth_node = head


        while k:
            if k and curr_node is None:
                return -1
            curr_node = curr_node.next
            k -= 1


        while curr_node:
            curr_node = curr_node.next
            kth_node = kth_node.next

        return kth_node.data


