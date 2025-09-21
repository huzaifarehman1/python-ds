"""
Create a hash table from scratch. Use chaining for hash collision
"""
# the size will be such that it will start size small and when full it will copy everything to the new bigger sized table

class HashTable:   
    class __node:
        def __init__(self,val,next = None):
            self.val = val
            self.next = next
        def __eq__(self, other):
            # Use self.__class__ so it's always the same node type
            if not isinstance(other, self.__class__):
                return False
            return self.val == other.val
    
    def __init__(self):
        self.__curr_size = 1000
        self.__hash_table = [None] * self.__curr_size


    def __insert(self,key,value):
        hash_value = self.hash_function(key)
        index = hash_value%self.__curr_size
        temp =self.__node((key,value))# so i can identify which node have the value
        
        if self.__hash_table[index] is None:
                self.__hash_table[index] = temp
        
        else:
            head = self.__hash_table[index]
            prev = head
            curr = head.next
            while curr is not None:
                curr = curr.next
                prev = prev.next
            assert prev.next is None
            prev.next = temp
                


    def __delete(self,ele):
        hash_value = self.hash_function(ele)
        index = hash_value%self.__curr_size
        if self.__hash_table[index] is None:
            return
        
        else:
            prev = None
            head = self.__hash_table[index]
            while head is not None:
                if head.val[0]==ele:
                    nex = head.next
                    while nex is not None:
                        
                        head.val = nex.val
                        prev = head
                        head = head.next
                        nex = nex.next                    
                    if prev is None:
                        # first element
                        temp = head.next
                        head.next = None
                        self.__hash_table = temp
                    else:
                        assert head.next is None
                        prev.next = None
                        del head    
                    return 
                
                prev = head
                head = head.next 
            return  
         


    def __get(self,ele):
        """access the value of ele = key"""
        hash_value = self.hash_function(ele)
        index = hash_value%self.__curr_size
        if self.__hash_table[index] == None:
            raise Exception("Error")

        head = self.__hash_table[index]
        while head is not None:
            if head.val[0] == ele:
                return head.val[1]
            head = head.next
        raise Exception("error")
                 
        
    def hash_function(self,ele):
        """return hash value for the ele"""
        # should support all data type such as tup int float str bool
        def for_int_float(ele):
                return (ele*10)+(pow(ele,2)//7) + ele 
            
        def for_str(ele):    
                
                    integer = 0
                    k = 1
                    for i in ele:
                        integer += k*(ord(i))
                        k += 1
                    ele = integer    
                    return (ele*10)+(pow(ele,2)//7) + ele 
                
        def for_tup(ele,total = 0):
            for i in ele:
                if isinstance(i,(int,float)):
                    answer =  for_int_float(i)   
                elif isinstance(i,str):
                    answer = for_str(i)
                elif isinstance(i,tuple):
                    answer = for_tup(i,total+1)
                else:
                    raise Exception(f"UNHASHABLE ITEM {ele}")
                total += answer
            return total 
        
        if isinstance(ele,(int,float)):
            return for_int_float(ele)   
        elif isinstance(ele,str):
            return for_str(ele)
             
        elif isinstance(ele,tuple):
            return for_tup(ele)
        else:
            raise Exception(f"UNHASHABLE ITEM {ele}")
        
    def __setitem__(self, key, value):
        self.__insert(key,value)  
    
    def __getitem__(self,key):
        return(self.__get(key))               

    def __delete__(self,key):
        self.__delete(key)
        
                    
                      