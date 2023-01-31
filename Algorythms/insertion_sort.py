#Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
class InsertionSort:


    def __init__(self, array):
        self.array = array


    def start_insertionSort(self):
        for step in range(1, len(self.array)):
            key = self.array[step]
            j = step - 1
                 
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j = j - 1
            self.array[j + 1] = key


    def talk(self):
        print(f"Insertion sorting in ascending order: {self.array} ")