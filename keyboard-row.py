class Solution(object):
    
    def find(self, each_word, s):
        for i in each_word:
            if i not in s:
                return False
        return True
        

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set(i for i in 'qwertyuiopQWERTYUIOP')
        s2 = set(i for i in 'asdfghjklASDFGHJKL')
        s3 = set(i for i in 'zxcvbnmZXCVBNM')
        ans = []
        print words
        for each_word in words:
            if each_word[0] in s1:
                if self.find(each_word, s1):
                    ans.append(each_word)
            elif each_word[0] in s2:
                if self.find(each_word, s2):
                    ans.append(each_word)
            elif each_word[0] in s3:
                if self.find(each_word, s3):
                    ans.append(each_word)
        return ans