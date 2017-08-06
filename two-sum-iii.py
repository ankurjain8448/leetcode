class Solution(object):
    def __init__(self):
        self.hash = {}
        self.current_index = -1

    def add(self, num):
        self.current_index += 1
        if num in self.hash:
            self.hash[num].append(self.current_index)
        else:
            self.hash[num] = [self.current_index]


    def find(self, num):
        for k, v in self.hash.iteritems():
            temp = num - k
            if temp in self.hash:
                values = self.hash[temp]
                if (v[0] != values[0]) or (v[0] == values[0] and len(values) > 1):
                    return True
        return False
