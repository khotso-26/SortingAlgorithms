
"""
QuickSort is a Divide and Conquer algorithm. 
It picks an element as a pivot and partitions the given array around the picked pivot.
"""
class SelectionSort:

    def __init__(self, array, size):
        self.array = array
        self.size = size

    def selectionSort(self):
    
        for step in range(self.size):
            min_idx = step

            for i in range(step + 1, self.size):
                if self.array[i] < self.array[min_idx]:
                    min_idx = i

        (self.array[step], self.array[min_idx]) = (self.array[min_idx], self.array[step])

    def talk(self):
        print(f"Select sorting in ascending order: {self.array}")