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

# Assumes the input is non-negative
def count_sort(nums, maximum):
    if min(nums) < 0 or max(nums) > maximum:
        raise ValueError("Please ensure that the minimum of nums is at least 0 and that the maximum of nums is equal to the maximum argument")
    
    sort_arr = [0 for _ in range(maximum+1)]
    for num in nums:
        sort_arr[num] += 1
     
    res = [0 for _ in range(len(nums))]
    for i in range(1, maximum+1):
        sort_arr[i] += sort_arr[i-1]

    for num in nums[::-1]:
        index = sort_arr[num] - 1
        res[index] = num
        sort_arr[num] -= 1
    
    return res

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

    count_sort_test = list(range(1000))
    random.shuffle(count_sort_test)
    count_sort_result = count_sort(count_sort_test, 1000)
    if count_sort_result == comp:
        print("Count Sort Success")
    else:
        print("Count Sort Failed")

if __name__ == "__main__":
    main()