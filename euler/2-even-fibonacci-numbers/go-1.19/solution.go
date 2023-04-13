package main

type s1 struct{}

// Naive solution O(n).
func (s1) EvenFibonacciNumbersSumUpTo(limit uint64) uint64 {
	var c uint64 = 2
	var p uint64 = 1
	var e uint64 = 0

	for c <= limit {
		if c%2 == 0 {
			e += c
		}
		var n uint64 = p + c
		p = c
		c = n
	}

	return e
}
