import algorythms.bubble_sort as bubble
import algorythms.insertion_sort as insertion
import algorythms.merge_sort as merge
import algorythms.quick_sort as quick
import algorythms.selection_sort as selection


if __name__ == "__main__":

    data = [70,1,42,563,3,-2,11,43]
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
