class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> mv;
        for(int i = 1; i <= n; i++){
            if (i%3 == 0 ){
                mv.push_back("Fizz");
                if (i%5 ==0)
                    mv[i-1] = "FizzBuzz";
            }
            else {
                if (i%5 ==0)
                    mv.push_back("Buzz");
                else{
                    mv.push_back(to_string(i));
                }
            }

        }
        return mv;
        
    }
};