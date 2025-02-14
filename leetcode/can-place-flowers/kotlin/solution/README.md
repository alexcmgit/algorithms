12m34s
O(N)
O(N)

Naive approach. Go through every item in the flowerbed and check if the adjacent items are set to 1, otherwise set the current place to 1 and set `free` plus 1 and continue next iteration. Make an early return if `free` is `>= n`
