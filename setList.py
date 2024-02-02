class SetList:
    class Node:

        # A constructor which stores a piece of data, reference to the SetList, a reference to the next Node and a reference to the previous Node.
        def __init__(self, data=None, set_list=None, next_node=None, prev_node=None):
            self.data = data
            self.set_list = set_list
            self.next_node = next_node
            self.prev_node = prev_node

        # Below are the member functions
        def get_data(self):       
            return self.data

        def get_next(self):
            return self.next_node

        def get_previous(self):
            return self.prev_node

        def get_set(self):
            return self.set_list

    # Aconstructor for setlist 
    def __init__(self):
        self.front = None
        self.back = None
        self.len = 0

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def make_set(self, data):
        if self.front is None:
            new = self.Node(data, self)
            self.front = new
            self.back = new
            self.len = self.len + 1
            return new
        return None

    def find_data(self, data):   # returns reference to the node
        curr = self.front
        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next_node
        return None

    def representative_node(self):
        return self.front

    def representative(self):
        if self.front is not None:
            return self.front.get_data()
        return None

    def union_set(self, other_set):           # In this function, elements of other_set are transfered to current object. Function returns number of elements transferred
        if other_set.front is not None:
            if self.front is None:
                self.front = other_set.front
                self.back = other_set.back
            else:
                self.back.next_node = other_set.front
                other_set.front.prev_node = self.back
                self.back = other_set.back

            self.len += other_set.len

            curr = other_set.front
            while curr is not None:
                curr.set_list = self
                curr = curr.next_node

            other_set.front = None
            other_set.back = None
            other_set.len = 0
            return self.len
        return 0

    def __len__(self):
        return self.len