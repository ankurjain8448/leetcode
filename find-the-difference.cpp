class Solution {
public:
    char findTheDifference(string s, string t) {
        char ans = 'a';
        int s_len = s.length(), t_len =  t.length();
        int max_size = t_len;
        
        int *arr = new int[26];
        for( int i = 0;i < 26 ; i++)
            arr[i] = 0;

        for(int i = 0;i < max_size -1 ; i++){
            arr[(int)s[i]-97]--;
            arr[(int)t[i]-97]++;
        }
        arr[(int)t[max_size-1]-97]++;
        
        for (int i = 0;i < 26 ; i++){
            if (arr[i] == 1){
                ans = (char)(i+97);
                break;
            }
                
        }
        return ans;
    }
};