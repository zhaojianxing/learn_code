import random


def sort_code1(nums):
    n = len(nums)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def sort_code2(nums):
    if not nums:
        return []
    else:
        key = nums[0]
        left = sort_code2([i for i in nums[1:] if i < key])
        right = sort_code2([j for j in nums[1:] if j >= key])
    return left+[key]+right

def sort_code3(nums):
    if len(nums) < 2:
        return nums
    # key = nums[0]
    key = random.choice(nums)
    left = []
    right = []
    for i in nums:
        if i < key:
            left.append(i)
        else:
            right.append(i)
    # return sort_code3(left) + [key] + sort_code3(right)
    return sort_code3(left)+sort_code3(right)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        字符串无重复子串
        定义三个变量 存放最后一个重复字符索引坐标，以及最后重复字符的长度，以及字典
        """
        di = dict()
        index, length = 0, 0
        for i in range(len(s)):
            if s[i] in di:
                index = max(di[s[i]], index)
            length = max(length, i-index+1)
            di[s[i]] = i + 1
        return length

class SolutionCode:
    """
    三数之和
    """
    def threeSum(self, nums):
        # """
        # 思路：双指针
        # """
        lists = []
        nums = sorted(nums)
        lens = len(nums)
        for i in range(lens):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tag = -nums[i]
            left = i+1
            rigth = lens-1
            while rigth > left:
                if nums[left] + nums[rigth] == tag:
                    lists.append([nums[i], nums[left], nums[rigth]])
                    while rigth > left and nums[left] == nums[left+1]:
                        left += 1
                    while rigth > left and nums[rigth] == nums[rigth-1]:
                        rigth -= 1
                    left += 1
                    rigth -= 1
                elif nums[left] + nums[rigth] < tag:
                    left += 1
                else:
                    rigth -= 1
        return lists


if __name__ == '__main__':
    nums = [3, 88, 34, 45, 21, 90, 1]
    li = [-1, 0, 1, 2, -1, -4]
    print(SolutionCode().threeSum(li))
    # num = sort_code1(nums)
    num = sort_code3(nums)
    print(num)