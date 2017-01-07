class Solution {
public:
    int reverse(int x) {
        int temp = x;
        vector<int> rev ;
        vector<int> rev_bin;
        long create_int = 0;
        long val = 1;
        
        x = abs(x);
        while(x){
        	rev.push_back(x%10);
        	x = x/10;
        }
        int size = rev.size();
        for(int i = 0;i< size;i++){
        	create_int = create_int + rev[size - 1 -i]*val;
        	val = val*10;
        }

        long t = create_int;
        while(t){
        	rev_bin.push_back(t%2);
        	t = t/2;
        }

        
        if (rev_bin.size() > 31)
        	return 0;
        else{
        	if (temp > 0)
        		return int(create_int);
        	else
        		return -int(create_int);
        }
        
    }
};