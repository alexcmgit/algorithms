# 215. Kth Largest Element in an Array

https://leetcode.com/problems/kth-largest-element-in-an-array/.

Given an integer array `nums` and an integer `k`, return the $k^{th}$ largest *element in the array*.

Note that it is the $k^{th}$ largest element in the sorted order, not the $k^{th}$ distinct element.

You must solve it in `O(n)` time complexity.

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:**

- $1 \le k \le nums.length \le 105.$
- $-104 \le nums[i] \le 104.$