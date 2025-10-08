---
timer: 1h48m
time_complexity: O(N)
space_complexity: O(N)
---

Naive solution. Extract all digits of `num`. Then brute force each digit replacement combination from 0 to 9. Store the max/min of it and return the difference.
