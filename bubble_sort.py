"""
Bubble sort is a sorting algorithm that compares two adjacent elements and 
swaps them until they are in the intended order.
"""
class bubbleSort:
    

    def __init__ (self, array):
        self.array = array


    def start_bubbleSort(self):
        for i in range(len(self.array)):
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = temp
    

    def talk(self):
        print(f"Bubble sorting in ascending order: {self.array}")