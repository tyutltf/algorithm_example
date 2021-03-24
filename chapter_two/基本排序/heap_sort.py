# 堆排序
import heapq


def heap_sort(nums):
    result = []
    for i in range(len(nums)):
        heapq.heapify(nums)
        result.append(nums[0])
        nums.remove(nums[0])

    return result


nums = [50, 36, 66, 76, 12, 25]
print(heap_sort(nums))
