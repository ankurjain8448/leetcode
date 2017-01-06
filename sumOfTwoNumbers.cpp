class Solution {
public:
    int getSum(int a, int b) {
        int a1 = a,b1 = b ;
        while (a&b){
            a1 = (a&b) << 1;
            b1 = a ^ b;
            a = a1;
            b = b1;
        }
        return a1|b1;
    }
};