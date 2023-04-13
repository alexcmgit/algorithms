int sum(int r, int n) => (n * (r + n * r)) >> 1;

// Doesn't support integers larger than 64 bits.
int multiplesOf3And5Below(int n) {
  final int e = n - 1;

  final int setA = sum(3, e ~/ 3);
  final int setB = sum(5, e ~/ 5);
  final int setC = sum(15, e ~/ 15);

  return setA + setB - setC;
}
