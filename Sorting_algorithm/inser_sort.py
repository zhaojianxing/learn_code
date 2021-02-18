def insertsort(nums):
    """
    插入排序：插入排序，不仅需要比较元素大小，还要移动元素。导致时间复杂度较高
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while(j >= 0 and key<nums[j]):
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

def bubblesort(nums):
    """
    冒泡排序：冒泡排序每次把剩余元素中确认最大的值移动到最终位置
    """
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

def quicksort(nums):
    """
    快速排序：递归法
    """
    if len(nums)==0:
        return nums
    key = nums[0]
    left = quicksort([i for i in nums if i < key])
    right = quicksort([i for i in nums if i >key])
    return left + [key] + right


if __name__ == '__main__':
    nums = [3, 9, 1, 10, 32, 44, 78, 21]
    print(insertsort(nums))
    print(bubblesort(nums))
    print(quicksort(nums))