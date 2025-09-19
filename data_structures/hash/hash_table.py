"""
Create a hash table from scratch. Use chaining for hash collision
"""
# the size will be such that it will start size small and when full it will copy everything to the new bigger sized table
class HashTable:   
    class __node:
        def __init__(self,val,next = None):
            self.val = val
            self.next = next
        def __eq__(self,other):
            if not(isinstance(other,HashTable.__node)):
                return False
            return self.val == other.val
        
    def __init__(self):
        self.hash_table = [] 
        self.__curr_size = 1000
        

    def check_collision(self):
        pass


    def add_to_linked_list(self):
        pass


    def insert(self):
        pass


    def delete(self):
        pass


    def get(self,ele):
        """access the value"""
        hash_value = self.hash_function(ele)
    
    def hash_function(self,ele):
        """return hash value for the ele"""
        # should support all data type such as tup int float str bool
            