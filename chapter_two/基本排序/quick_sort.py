# 快速排序
def quicksort(nums, low, high):
    if low < high:
        i = low
        j = high
        key = nums[i]
        # 一趟快速排序
        while i < j:
            while i < j and key <= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

            while i < j and key >= nums[i]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
            print(nums)
        quicksort(nums, low, i-1)
        quicksort(nums, i+1, high)
        return nums


'''
def swap(list, i, j):
    """位置互换"""
    list[i], list[j] = list[j], list[i]
    return list


def quicksort(list, start, end):
    if start < end:
        i, j = start, end
        base = list[i]  # 设置基数
        while i < j:
            while i < j and list[j] >= base:  # 从后往前找
                j -= 1
            swap(list, i, j)  # 当找到比基数小的数与其互换位置

            while i < j and list[i] <= base:  # 从前往后找
                i += 1
            swap(list, i, j)  # 当找到比基数大的数与其互换位置

        # 递归
        quicksort(list, start, i-1)
        quicksort(list, j+1, end)
        return list
'''

nums = [50, 36, 66, 76, 12, 25]
print(quicksort(nums, 0, len(nums)-1))

'''
key 左边都小于key key右边都大于key 时间复杂度为 O(nlog2n)
'''
