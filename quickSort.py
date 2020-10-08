"""
File: quickSort.py

Recursive implementation of quickSort
"""

import random
import time

def quickSort(aList):
    quickSortHelper(aList, 0, len(aList) - 1)

def quickSortHelper(aList, left, right):
    if left < right:
        pivotLocation = partition(aList, left, right)
        quickSortHelper(aList, left, pivotLocation - 1)
        quickSortHelper(aList, pivotLocation + 1, right)

def partition(aList, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = aList[middle]
    aList[middle] = aList[right]
    aList[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if aList[index] < pivot:
            temp = aList[index]
            aList[index] = aList[boundary]
            aList[boundary] = temp
            boundary += 1
    # Exchange the pivot item and the boundary item
    temp = aList[boundary]
    aList[boundary] = aList[right]
    aList[right] = temp
    return boundary


