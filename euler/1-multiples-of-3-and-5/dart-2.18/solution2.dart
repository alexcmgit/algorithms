// Lead to floating errors when [n] or the result of
// this operations is bigger than 64 bits.
// A [BigInt] implementation is required to handle that edge cases.
int sum(int r, int n) => (n * (r + n * r)) ~/ 2;

// Doesn't support integers larger than 64 bits.
int multiplesOf3And5Below(int n) {
  final int e = n - 1;

  final int setA = sum(3, e ~/ 3);
  final int setB = sum(5, e ~/ 5);
  final int setC = sum(15, e ~/ 15);

  return setA + setB - setC;
}
