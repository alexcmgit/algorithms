---
timer: 11m16s
time_complexity: O(N)
space_complexity: O(N)
---

To see if a string1 is divisible by another string2 just string1.replaceAll(string2, "").

Then using the above trick try on both str1 and str2 strings, if they both pass then its divisible by the two, otherwise try again trimming the last char.

obs. Not proud of this solution, tried to finish as fast as possible.
