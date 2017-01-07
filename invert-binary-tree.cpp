/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    TreeNode* invertTree(TreeNode* root) {
        
        queue<TreeNode*> q;
        TreeNode* temp = root;
        TreeNode* temp1 = root;
        
        if (root) q.push(root);
        while(!q.empty()){
            temp = q.front();
            q.pop();
            temp1 = temp->left;
            temp->left = temp->right;
            temp->right = temp1;
            if (temp->right)
                q.push(temp->right);
            if (temp->left)
                q.push(temp->left);
        }
        return root;
        
    }
};