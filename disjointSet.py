from setList import SetList

class DisjointSet:
    def __init__(self):
        self.elements = {} # Dictionary to store elements and their corresponding set lists

    def make_set(self, element):
        if element in self.elements: # Check if the element already exists in any set
            return False
        else:
            new_set_list = SetList() # Create a new SetList object
            new_set_list.make_set(element) # Add the element to the new set
            self.elements[element] = new_set_list # Store the element and its set list in the dictionary
            return True

    def get_set_size(self, element):
        set_list = self.find_set(element)  # Find the set list containing the element
        if set_list is None:
            return 0
        return len(self.elements[set_list]) # Return the size of the set list

    def find_set(self, element):
        for key, set_list in self.elements.items():  # Iterate over the elements and their set lists
            if set_list.find_data(element) is not None:  # Check if the element exists in the set list
                return key # Return the key (representative element) of the set list
        return None # Return None if the element is not found in any set list

    def union_set(self, element1, element2):
        if self.elements[element1].find_data(element2) is not None:  # Check if the elements are already in the same set
            return False

        tmp = None
        for key, set_list in self.elements.items():  # Find the set list containing element2
            if set_list.find_data(element2) is not None:
                tmp = set_list.find_data(element2)
                break

        self.elements[element1].union_set(tmp.get_set())  # Merge the set containing element2 into the set containing element1

        if element2 in self.elements:
            self.elements.pop(element2)  # Remove element2 from the dictionary if it is a key
        else:
            self.elements.pop(tmp.get_set().get_front().get_next().get_data()) # Remove the element following the front of the set list

        return True

    def get_num_sets(self):
        return len(self.elements) # Return the number of sets (number of elements in the dictionary)

    def __len__(self):
        size = 0
        for element in self.elements:
            size += len(self.elements[element]) # Compute the total number of elements in all sets
        return size