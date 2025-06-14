

// User function Template for Java

/*Complete The Function Provided
Given Below is The Node Of Tree
class Node
{
    int data;
    Node left, right;
    public Node(int data)
    {
        this.data = data;
         left = right = null;
    }
}*/

class Solution {
    // Function to return list containing elements of right view of binary tree.
    int maxLevel = -1;
    ArrayList<Integer> rightView(Node root) {
        // add code here.
        ArrayList<Integer> list = new ArrayList<>();
        rightView(root, list, 0);
        return list;
    }
    
    void rightView(Node node, ArrayList<Integer> list, int level){
        if(node != null){
            if(maxLevel < level){
                list.add(node.data);
                maxLevel = level;
            }
            
            rightView(node.right, list, level+1);
            rightView(node.left, list, level+1);
        }
    }
}