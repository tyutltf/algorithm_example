# 冒泡排序
def bubblesort(nums):
    for i in range(len(nums)-1):
        flag = 0
        for j in range(len(nums)-1-i):
            # 大元素往后移动
            if nums[j] > nums[j+1]:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
                flag = 1
        if flag == 0:
            break
    return nums


nums = [1, 5, 3, 18, 29, 15, 30]
print(bubblesort(nums))

'''
冒泡排序，即每一次循环，找出最大的，放在数组最后一位 时间复杂度为 O(n)2 空间复杂度为 O(1)
'''
