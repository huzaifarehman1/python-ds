class Queue:
    """
    Queue is an abstract data structure, somewhat similar to Stacks.
    Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue)
    and the other is used to remove data (dequeue).
    Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first.

    """
    class __Node: # new addition
        """ used for double linked list logic of queue"""
        """ should not available outside the class"""
        def __init__(self,element,next = None,prev = None):
            self.ele = element
            self.next = next
            self.prev = prev

    def __init__(self): # modified part
        
        self.head = None # points to last pushed element (enqueue part)
        self.length = 0 # number of elements in it
        self.Tail = None # points to first pushed element (dequeue part)
    
    def is_empty(self): # new addition
        """check is queue object is empty or not
        return boolean
        """
        return self.length<=0
            
    def put(self, item): # modified part
        """add item to queue

        Args:
            item (any): item to be  pushed
        """
        temp = self.__Node(item) # create new node
        
        if self.is_empty():
            # initialize the doubly linked list
            self.head = temp
            self.Tail = temp
            
            self.length += 1 
            return 
        # already initialized so just add the item

        self.head.next = temp # point to next element
        self.head = self.head.next # move pointer to next element which is last pushed element
         
        self.length += 1 
        return 
            
    def get(self):
        if self.length <= 0:
            return
        self.length -= 1
        de_queued = self.entries[self.front]
        self.entries = self.entries[1:]
        return de_queued

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    def size(self):
        return self.length

    def __len__(self): # new addition
        return self.length    