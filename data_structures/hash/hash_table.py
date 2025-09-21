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
        temp =self.__node(value)
        
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
                


    def delete(self,ele):
        hash_value = self.hash_function(ele)
        index = hash_value%self.__curr_size
         


    def get(self,ele):
        """access the value of ele = key"""
        
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
                if isinstance(ele,(int,float)):
                    answer =  for_int_float(ele)   
                elif isinstance(ele,str):
                    answer = for_str(ele)
                elif isinstance(ele,tuple):
                    answer = for_tup(ele,total+1)
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
                    
                    
                
            