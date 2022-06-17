
def Solution(nums):
    head = 0
    current = 0
    tail = len(nums) - 1
    while current <= tail:
        if nums[current] < 1:
            nums[current], nums[head] = nums[head], nums[current]
            head += 1
            current += 1
        elif nums[current] > 1:
            nums[current], nums[tail] = nums[tail], nums[current]
            tail -= 1
        else:
            current += 1
    return nums


nums = [2, 1, 0, 2, 1, 1, 2, 0]
print(Solution(nums))
