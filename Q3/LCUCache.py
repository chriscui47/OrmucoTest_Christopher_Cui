import time
class Node:
    def __init__(self, key, value,start):
        self.key=key
        self.value=value
        self.prev=None 
        self.next=None
        self.start=start
    

class LRUCache:
    
    def __init__(self,capacity,maxTime):
        self.dict=dict()
        self.capacity=capacity
        self.head=Node(0,0,-1000)
        self.tail=Node(0,0,-1000)
        self.head.next=self.tail
        self.tail.prev=self.head
        #enter maxtime in seconds
        self.maxTime=maxTime
    #popping from head
    
    def checkTime(self,node):
        elapsed = time.time() - node.start
        if elapsed>self.maxTime and len(self.dict)!=0:
            self.timeout(node)
            return False
        else:
            return True

    def get(self,key):
        if key in self.dict:
            node=self.dict[key]
            self._delete(node)
            #we add it back, to refresh the position on the list
            #because its recently used
            self._add(node)
            return node.value
        self.checkTime(self.head.next)
        #if not inside dict return -1
        return -1


    def put(self,key,value):
        if key in self.dict:
            self._delete(self.dict[key])
        node=Node(key,value,time.time())
        #add to tail off list (becomes newest item)
        self._add(node)
        self.dict[key]=node
        if (len(self.dict)>self.capacity):
            #delete from the head of the list (the least used tiem)
            node=self.head.next
            self._delete(node)
            del self.dict[node.key]
            #WE ALWAYS check time of least used item to see if it is time to expire
        self.checkTime(self.head.next)
    def _delete(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    def timeout(self,node):
        if node.prev==self.head and (node==self.head or node==self.tail):
            self.head.next=self.tail
            self.tail.prev=self.head
            del self.dict[node.key]
        else:
            prev=node.prev
            next=node.next
            prev.next=next
            next.prev=prev
            del self.dict[node.key]

    #adding to tail dummy
    def _add(self,node):
        prev=self.tail.prev
        prev.next=node
        self.tail.prev=node
        node.prev=prev
        node.next=self.tail
        self.checkTime(self.head.next)
        return -1

obj=LRUCache(10,5)
obj.put(10,2)
print(obj.get(10))
