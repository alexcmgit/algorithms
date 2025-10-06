---
time: 20m
time_complexity: O(N)
space_complexity: O(N)
---

Create `rows` string buffers to store the chars of each row individually.

Use a pointer `y` to track the current row index of the current char.

Write the current char at the string buffer of the current row index.

Merge/fold all string buffers and return it.
