# [Design HashMap] https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.hmap = {}

    def put(self, key: int, value: int) -> None:
        self.hmap[key] = value

    def get(self, key: int) -> int:
        return self.hmap[key] if key in self.hmap else -1

    def remove(self, key: int) -> None:
        self.hmap.pop(key, None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
