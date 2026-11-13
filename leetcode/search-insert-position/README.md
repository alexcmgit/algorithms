
# 35. Search Insert Position

**Difficulty:** Easy  
**Topics:** Array, Binary Search  
**Source:** [LeetCode](https://leetcode.com/problems/search-insert-position/description/)

## Problem Description

Given an array `nums` containing unique integers sorted in ascending order and an integer `target`, determine the index where `target` belongs.

- If `target` exists in the array, return its index.
- Otherwise, return the index where it could be inserted while preserving the sorted order.

The algorithm must have a time complexity of **O(log n)**.

## Examples

### Example 1

**Input:**
```text
nums = [1,3,5,6]
target = 5
```

**Output:**
```text
2
```

### Example 2

**Input:**
```text
nums = [1,3,5,6]
target = 2
```

**Output:**
```text
1
```

### Example 3

**Input:**
```text
nums = [1,3,5,6]
target = 7
```

**Output:**
```text
4
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- All elements in `nums` are distinct and sorted in ascending order.
- `-10^4 <= target <= 10^4`
