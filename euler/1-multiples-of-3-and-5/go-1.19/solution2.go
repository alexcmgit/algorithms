package main

type s2 struct{}

// Naive multiples of 3 and 5 [complexity O(n)].
func (s2) MultiplesOf3And5Below(n int64) int64 {
	var i int64 = 0
	var sum int64 = 0

	for i < n {
		if i%3 == 0 {
			sum += i
		} else if i%5 == 0 {
			sum += i
		}

		i++
	}

	return sum
}
