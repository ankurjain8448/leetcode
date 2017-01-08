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
    int find_sum(TreeNode* root, int ans){
        if (root){
            
            if (root->left){
                if (root->left->left == NULL && root->left->right == NULL)
                    ans = ans + root->left->val;
                ans = find_sum(root->left, ans);
            }
            if (root->right)
                ans = find_sum(root->right, ans);
        }
        return ans;
    }
    int sumOfLeftLeaves(TreeNode* root) {
     return find_sum(root, 0);   
    }
};