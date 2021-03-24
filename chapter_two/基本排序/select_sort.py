# 简单选择排序
def selectsort(nums):
    for i in range(len(nums)):
        min_position = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                min_position = j
                if i != min_position:
                    nums[j], nums[i] = nums[i], nums[j]
    return nums


nums = [50, 36, 66, 76, 12, 25]
print(selectsort(nums))

'''
时间复杂度 O(n)2 每一趟找出一个最小的放在应该的位置
'''
