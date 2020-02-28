import time
import re
class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.prev=None 
        self.next=None
        self.start=time.time()
    

class GeoLRUCache:
    
    def __init__(self,capacity,maxTime):
        self.dict=dict()
        self.capacity=capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        #enter maxtime in seconds
        self.maxTime=maxTime

    #We call this funciton to verify if node time expired    
    def checkTime(self,node):
        elapsed = time.time() - node.start
        if elapsed>self.maxTime and len(self.dict)!=0:

            self.timeout(node)
            return False
        else:
            return True

    def get(self,key):
        #everytime we get, we scan thru whole list to check if any expried. if so, then delete
        curr=self.head.next
        if (curr!=self.head and curr!=self.tail):
            while(curr!=self.tail):
                self.checkTime(curr)
                curr=curr.next
        if key in self.dict:
            node=self.dict[key]
            self._delete(node)
            #we add it back, to refresh the position on the list
            #because its recently used
            self._add(node)
            return node.value
        #if not inside dict return -1

        return("Item not in dict or expired")

    def put(self,key,value):
    #verify valid input
        if  not (isinstance(key, int)):
            return ("Numbers only for key!")
        if key==None or value == None:
            return("Empty input")
        
        if key in self.dict:
            self._delete(self.dict[key])
        node=Node(key,value)
        #add to tail off list (becomes newest item)
        self._add(node)
        self.dict[key]=node
        if (len(self.dict)>self.capacity):
            #delete from the head of the list (the least used tiem)
            node=self.head.next
            self._delete(node)
            del self.dict[node.key]
            
    def _delete(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    def timeout(self,node):
        #if the node is not the head, we delete it
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
        return -1
