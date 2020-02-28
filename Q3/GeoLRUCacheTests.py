import unittest
import time
from GeoLRUCache import GeoLRUCache
import json
class TestCache(unittest.TestCase):
    def test_Get_Value(self):
        cache = GeoLRUCache(4,20)
        cache.put(1,"hello")
        self.assertEqual("hello", cache.get(1))
        cache.put(2, 131)
        self.assertEqual(131, cache.get(2))

    def test_Get_Value_Error(self):
        cache = GeoLRUCache(1,20)
        self.assertEqual("Item not in dict or expired",cache.get(1))
        cache.put(1, "AFAAFA")
        cache.put(2, "FAFAFA")
        self.assertEqual("Item not in dict or expired",cache.get(1))

    def test_Put_Value(self):
        cache = GeoLRUCache(4,20)
        cache.put(1, "hello")
        self.assertEqual("hello", cache.get(1))
        cache.put(2, "world")
        self.assertEqual("world",cache.get(2))


    def test_put_error(self):
        cache = GeoLRUCache(5,20)
        self.assertEqual(cache.put(1,None), "Empty input")
    
    def test_Expiration(self):
        cache = GeoLRUCache(1,2)
        cache.put(1, "hii")
        self.assertEqual("hii",cache.get(1))
        time.sleep(3)
        self.assertEqual(cache.get(1),"Item not in dict or expired")
        

if __name__ == '__main__':
    unittest.main()