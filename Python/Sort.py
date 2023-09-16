import random

def bubble_sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length-i-1): # We could also do range(length), but this is a nice optimization
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # Swapping done in a nice pythonic way

def insertion_sort(nums):
    length = len(nums)
    for i in range(length):
        j=i
        while j>0 and nums[j-1]>nums[j]: # The second part is an optimization, we don't technically need it
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

def selection_sort(nums):
    length = len(nums)
    for i in range(length):
        index = i
        for j in range(i+1, length):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]

def merge(a, b):
    array = []
    size_a = len(a)
    size_b = len(b)
    j, k = 0, 0
    while j < size_a and k < size_b:
        if a[j] < b[k]:
            array.append(a[j])
            j+=1
        else:
            array.append(b[k])
            k+=1
    array.extend(a[j:])
    array.extend(b[k:])
    return array

def merge_sort(nums):
    if len(nums) in [0,1]:
        return nums
    middle = len(nums)//2
    left = nums[:middle]
    right = nums[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def partition(array, pivot):
    j = 0
    array[pivot], array[-1] = array[-1], array[pivot]
    for i in range(pivot-1):
        if array[i] < array[-1]:
            array[i], array[j] = array[j], array[i]
        j += 1
    array[-1], array[j] = array[j], array[-1]

def quicksort(nums):
    pass

def main():
    comp = list(range(1000))

    bubble_test = list(range(1000))
    random.shuffle(bubble_test)
    bubble_sort(bubble_test)
    if bubble_test == comp:
        print("Bubble Sort Success")
    else:
        print("Bubble Sort Failed")

    insertion_test = list(range(1000))
    random.shuffle(insertion_test)
    insertion_sort(insertion_test)
    if insertion_test == comp:
        print("Insertion Sort Success")
    else:
        print("Insertion Sort Failed")

    selection_test = list(range(1000))
    random.shuffle(selection_test)
    selection_sort(selection_test)
    if selection_test == comp:
        print("Selection Sort Success")
    else:
        print("Selection Sort Failed")

    merge_sort_test = list(range(1000))
    random.shuffle(merge_sort_test)
    merge_sort_result = merge_sort(merge_sort_test)
    if merge_sort_result == comp:
        print("Merge Sort Success")
    else:
        print("Merge Sort Failed")

if __name__ == "__main__":
    main()