import random

def bubble_sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length-i-1): # We could also do range(length), but this is a nice optimization
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # Swapping done in a nice pythonic way
    
    return nums

def insertion_sort(nums):
    length = len(nums)
    for i in range(length):
        j=i
        while j>0 and nums[j-1]>nums[j]: # The second part is an optimization, we don't technically need it
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

    return nums

def main():
    comp = list(range(1000))
    test = list(range(1000))
    random.shuffle(test)

    bubble_sorted = bubble_sort(test.copy())
    if bubble_sorted == comp:
        print("Bubble Sort Success")
    else:
        print("Bubble Sort Failed")

    insertion_sorted = insertion_sort(test.copy())
    if insertion_sorted == comp:
        print("Insertion Sort Success")
    else:
        print("Insertion Sort Failed")

if __name__ == "__main__":
    main()