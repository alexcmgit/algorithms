---
timer: 2h
time_complexity: O(N)
space_complexity: O(N)
---

Its more a linked list problem than a math problem.

Apply sum method and save the remainder to the next iteration.

The tricky part is to create the result linked list in reverse order. To do so save the linked list head pointer at the first result and make a dummy/temp linked list pointer to the fill the result of the next digits.

<img width="654" height="113" alt="image" src="https://github.com/user-attachments/assets/3cfdb25d-188d-42c9-8e90-9082c30b1f68" />

