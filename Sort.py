import random

def bubble_sort(nums):
    length = len(nums)

    for i in range(length):
        for j in range(length-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def main():
    comp = list(range(1000))
    test = list(range(1000))
    random.shuffle(test)

    sorted = bubble_sort(test)
    
    if sorted == comp:
        print("Bubble Sort Success")
    else:
        print("Bubble Sort Failed")

if __name__ == "__main__":
    main()