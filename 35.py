# Leetcode 35 - Search Insert Position

from typing import List

def searchInsert(nums:List[int], target: int) -> int:

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l+r) // 2

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return l

# driver code
res = searchInsert([1,3,5,6], 7)
print(res)
