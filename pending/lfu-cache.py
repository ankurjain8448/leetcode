class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_capacity = capacity
        self.cache = {}
        self.capacity = 0
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cache.get(key,None)
        return value
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.get(key):
            if self.capacity == self.max_capacity:
                pass
            else:
                self.cache[key] = value
        else:
            pass


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)