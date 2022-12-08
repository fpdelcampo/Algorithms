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

if __name__ == "__main__":
    main()