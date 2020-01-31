from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            # remove item at head
            remove_me = self.storage.head
            self.storage.remove_from_head()
            # add new item to tail
            self.storage.add_to_tail(item)
            if remove_me == self.current:
                self.current = self.storage.tail

        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item) 
            self.current = self.storage.head   
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage.length == 0:
            return 'Empty'

        
        active_node = self.current
        list_buffer_contents.append(active_node.value)    

        
        if active_node.next:
            next_node = active_node.next
        else:
            next_node = self.storage.head

       
        while next_node != active_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head    


        return list_buffer_contents       

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
