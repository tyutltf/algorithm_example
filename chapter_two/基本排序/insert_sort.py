# 直接插入排序
def insertsort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums


nums = [1, 5, 3, 18, 29, 15, 30]
print(insertsort(nums))

'''
不仅需要比大小，还需要移动元素，复杂度比较高 1/2 n*(n+1) -1 = O(n)方
'''
