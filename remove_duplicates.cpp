/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *start = head;
        ListNode *temp = head;
        while(start){
            while ( start->next && (start->val == start->next->val)){
                temp = start->next;
                start->next = temp->next;
            }
            start = start->next;
        }
        return head;
    }
};
