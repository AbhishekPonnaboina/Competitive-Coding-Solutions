

// User function Template for Java
class Solution {
    Node find(int[]in,int post[],int left,int right,ArrayList<Integer> list){
       if(list.get(0) == -1 || left > right)return null;
       int mid = 0;
       for(int i = left ; i <= right ; i++){
           if(in[i] == post[list.get(0)]){
               mid = i;
               break;
           }
       }
       int t = list.get(0);
       list.remove(0);
       list.add(t-1);
       Node rootN = new Node(in[mid]);
       rootN.right = find(in,post,mid+1,right,list);
       rootN.left = find(in,post,left,mid-1,list);
       return rootN;
    }
   Node buildTree(int[] inorder, int[] postorder) {
       // code here
       int n =inorder.length;
        ArrayList<Integer> list = new ArrayList<>();
       list.add(n-1);
       return find(inorder,postorder,0,n-1,list);
   }
}