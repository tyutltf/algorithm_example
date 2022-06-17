'''
给定一个包含红色 白色 蓝色的一共n个元素的数组，原地对他们进行排序，使相同颜色的元素相邻，并按照红白蓝顺序排列，这里使用012分别表示红白蓝
'''


def Solution(nums):
    num0 = num1 = num2 = 0
    for num in nums:
        if num == 0:
            num0 += 1
        if num == 1:
            num1 += 1
        if num == 2:
            num2 += 1
    for i in range(num0):
        nums[i] = 0
    for i in range(num0, num0+num1):
        nums[i] = 1
    for i in range(num0+num1, len(nums)):
        nums[i] = 2
    return nums


nums = [2, 1, 0, 2, 1, 1, 2, 0]
print(Solution(nums))
