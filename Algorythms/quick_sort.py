""" 
QuickSort is a Divide and Conquer algorithm. 
It picks an element as a pivot and partitions the given array around the picked pivot.
"""
class QuickSort(object):

    def __init__(self, array, high, low):
        self.array = array
        self.high = high
        self.low = low


    def partition(self, array, low, high):

        pivot = self.array[high]

        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i = i + 1

            (self.array[i], self.array[j]) = (self.array[j], self.array[i])
        (self.array[i + 1], self.array[high]) = (self.array[high], self.array[i + 1])

        return i + 1

    def quickSort(self):
        if self.low < self.high:

            pi = self.partition(self.array, self.low, self.high)
            QuickSort(self.array, self.low, pi - 1)
            QuickSort(self.array, pi + 1, self.high) 
    
    def talk(self):
        print(f"Quick sorting in ascending order: {self.array}")