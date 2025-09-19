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
        self.hash_table = [None] * self.__curr_size

    def check_collision(self):
        pass


    def add_to_linked_list(self):
        pass


    def insert(self):
        pass


    def delete(self):
        pass


    def get(self,ele):
        """access the value of ele = key"""
        hash_value = self.hash_function(ele)
    
    def hash_function(self,ele):
        """return hash value for the ele"""
        # should support all data type such as tup int float str bool
        def for_int_float(ele):
                return (pow(ele,3)*10)-(pow(ele,2)//7) - ele 
            
        def for_str(ele):    
                
                    integer = 0
                    k = 1
                    for i in ele:
                        integer += k*(ord(i))
                        k += 1
                    ele = integer    
                    return (pow(ele,3)*10)+(pow(ele,2)//7) - ele 
        def for_tup(ele):
            total = 0
            k = True
            for i in ele:
                if isinstance(ele,(int,float)):
                    answer =  for_int_float(ele)   
                elif isinstance(ele,str):
                    answer = for_str(ele)
                
        if isinstance(ele,(int,float)):
            return for_int_float(ele)   
        elif isinstance(ele,str):
            return for_str(ele)
             
        elif isinstance(ele,tuple):
            
                    
                    
                    
                
            