# 折半插入排序
def half_insertsort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        high = i-1
        low = 0
        # 折半查找元素应该插入的位置
        while (low <= high):
            mid = int((low+high)/2)
            if key >= nums[mid]:
                low = mid+1
            if key < nums[mid]:
                high = mid-1
        j = i-1
        # 移动元素的过程
        while j >= low:
            nums[j+1] = nums[j]
            j -= 1
        nums[low] = key
    return nums


nums = [1, 5, 3, 18, 29, 15, 30]
print(half_insertsort(nums))

'''
折半插入排序即将插入排序里的比较部分 使用了二分比较 不过总的时间复杂度仍然为 O(n)2
'''
