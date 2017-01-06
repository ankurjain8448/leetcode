class Solution {
public:
    int hammingDistance(int x, int y) {
        int ans = 0;
        y = y^x;
        while (y > 0){
            if (y%2 == 1)
                ans += 1;
            y = y/2;
        }
        return ans;
    }
};
