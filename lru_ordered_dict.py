from collections import OrderedDict

class LRUCache:
    ''' initializing capacity'''
    def __init__(self, capacity:int):
        self.cache = OrderedDict()
        self.capacity = capacity

    ''' We return the value of the key
    that is queied in O(1) and return -1 if
    we don't find the key in our dict/cache.
    Adn we also move the ey to the end
    to show that they key was recently used'''
    def get(self, key:int)->int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    ''' first we add/update the key by conventional methods.
    And also move the key to the end yo show that it was recently
    used. But here we will also check the length of our ordered
    dictionary has exceeded capacity, if so we remove the least
    recently used key'''
    def put(self, key:int, value:int)->None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            # the last flag is set to false so that it is popped in FIFO manner
            self.cache.popitem(last = False)

# Runner
# initializing the  cache with capacity 2
cache = LRUCache(2)

cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)



