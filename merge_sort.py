# Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
class MergeSort(object):


    def __init__(self, array):
        self.array = array
    

    def start_mergeSort(self):

        if len(self.array) > 1:

            r = len(self.array)//2
            left = self.array[:r]
            right = self.array[r:]

            leftSorter = MergeSort(left)
            leftSorter.start_mergeSort()
            leftSorter = MergeSort(right)
            leftSorter.start_mergeSort()

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.array[k] = left[i]
                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1


    def talk(self):
        print(f"Merge sorting in ascending order: {self.array}")