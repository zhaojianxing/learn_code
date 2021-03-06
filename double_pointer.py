# conding=utf-8
"""
双指针算法：
1）双指针法：一个指向头部，一个指向尾部，向中间靠拢
2）快慢双指针：两个指针在相同的起始位置。遍历过程中，行进的速度不相同。一快一慢。
3）后序双指针法：遍历过程中从后向前遍历。与常规的从头开始遍历不同的目的在于避免改变或者覆盖之前的数据
"""


def threeSum(nums):
    """
    双指针
    三数求和为0
    """
    nums = sorted(nums)
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums)-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            else:
                right -= 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
    return result

def fourSum(nums):
    """
    双指针
    四数求和：在三数求和的基础上，增加一层循环，变成三数求和
    """
    nums = sorted(nums)
    result = []
    ls = len(nums)
    for i in range(ls-3):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, ls-2):
            left = j + 1
            right = ls - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                # print("sum: %d"%(s))
                # print("left: %d"%(left))
                # print("right: %d"%(right))     
                if s == 0:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif s < 0:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1 
    return result


def maxArea(nums):
    """
    双指针法
    最大容积
    """
    res = 0
    left = 0
    right = len(nums)-1
    while left < right:
        res = max(res, min(nums[left], nums[right])*(right-left))
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return res


def liftboat(weights, limit_weight):
    """
    双指针法：快艇问题
    """
    weights = sorted(weights)
    n = 0
    ls = len(weights)
    if ls == 0:
        return n
    n = 1
    left = 0
    right = ls - 1
    while left < right:
        s = weights[left] + weights[right]
        n += 1
        if s <= limit_weight:
            left += 1
        else:
            right -= 1 
    return n

# 快慢指针法 
def movezeroes(nums):
    """
    快指针指向不为零的元素，慢指针指向零元素，满足条件就交换
    快指针每一步都会增加，直到为不为零的元素；
    慢指针碰到零元素则对准它；
    如果慢指针对零，而快指针非零，则交换，然后指针各加1；
    """
    slower = 0
    faster = 0
    ls = len(nums)
    while faster <= ls:
        if nums[slower] != 0:  # 慢指针指向零元素
            slower += 1
        elif nums[faster] != 0:  # 快指针指向不为零的元素
            nums[slower], nums[faster] = nums[faster], nums[slower]
            slower += 1
        faster += 1
    return nums

if __name__ == '__main__':
    nums_1 = [-1, 0, 1, 2, -1, -4]
    nums_2 = [1, 0, -1, 0, -2, 2]
    nums_3 = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    weights = [3, 5, 3, 4]
    limit_weight = 5
    print(threeSum(nums_1))
    print(fourSum(nums_2))
    print(maxArea(nums_3))
    print(liftboat(weights, limit_weight))
    print(movezeroes(nums_2))