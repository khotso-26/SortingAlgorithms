import Algorythms.bubble_sort as bubble
import Algorythms.insertion_sort as insertion
import Algorythms.merge_sort as merge
import Algorythms.quick_sort as quick
import Algorythms.selection_sort as selection


if __name__ == "__main__":

    data = [ 5, -2, 23, 7, 87, -42, 509 ]
    size = len(data)

    bubbleSorting = bubble.bubbleSort(data)
    bubbleSorting.start_bubbleSort()
    bubbleSorting.talk()

    insertionSort = insertion.InsertionSort(data)
    insertionSort.start_insertionSort()
    insertionSort.talk()

    mergeSort = merge.MergeSort(data)
    mergeSort.start_mergeSort()
    mergeSort.talk()

    quickSort = quick.QuickSort(data, 0, size-1)
    quickSort.talk()

    selectionSort = selection.SelectionSort(data, size)
    selectionSort.talk()
