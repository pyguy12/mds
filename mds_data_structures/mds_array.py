from mds_data_structures.mds_data_structure import MDSLinearDataStructure

class MDSArray(MDSLinearDataStructure):
    def __init__(self, *elements):
        self.array = list(elements)

    def __getitem__(self, index):
        # Manim code to animate element access
        pass
        return self.array[index]

    def __setitem__(self, index, value):
        # Manim code to animate element setting
        pass
        self.array[index] = value

    def __delitem__(self, index):
        # Manim code to animate element deletion
        pass
        del self.array[index]

    def __len__(self):
        return len(self.array)
    
    def __contains__(self, value):
        # Manim code to animate element search
        return value in self.array
    
    def index(self, value):
        # Manim code to animate index retrieval
        return self.array.index(value)
    
    def count(self, value):
        # Manim code to animate count operation
        return self.array.count(value)

    def extend(self, iterable):
        # Manim code to animate extending
        self.array.extend(iterable)

    def pop(self, index=None):
        # Manim code to animate pop operation
        if index is None:
            return self.array.pop()
        else:
            return self.array.pop(index)

    def reverse(self):
        # Manim code to animate reversing
        self.array.reverse()

    def sort(self):
        # Manim code to animate sorting
        self.array.sort()

    def insert(self, index, value):
        # Manim code to animate insertion
        pass
        self.array.insert(index, value)

    def append(self, value):
        # Manim code to animate appending
        pass
        self.array.append(value)

    def visualize(self):
        # Manim code to animate the final state of the array
        pass
