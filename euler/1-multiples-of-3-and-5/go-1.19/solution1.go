package main

type s1 struct{}

func sum(r int64, n int64) int64 {
	return (n * (r + n*r)) >> 1
}

// Fast multiples of 3 and 5 using AP [complexity O(1)].
func (s1) MultiplesOf3And5Below(n int64) int64 {
	var e int64 = n - 1

	var setA int64 = sum(3, e/3)
	var setB int64 = sum(5, e/5)
	var setC int64 = sum(15, e/15)

	return setA + setB - setC
}
