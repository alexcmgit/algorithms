extension PermutationCount<T> on List<T> {
  // Permutation count is a simple factorial:
  int permutationCount() {
    int count = 1;
    // Linear time O(n), max permutation count size: 2^64 bits.
    for (int i = length; i > 1; i--) {
      count *= i;
    }
    return count;
  }
}

int permutationCount(int x) =>
    List<int>.generate(x, (int index) => index + 1).permutationCount();
