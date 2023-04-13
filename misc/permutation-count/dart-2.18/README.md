This solution is an extension of an `Iterable<T>` that returns the `permutationCount()` by calculating the factorial of the iterable length.

```dart
void main() {
  print([].permutationCount()); // 1.
  print([1].permutationCount()); // 1.
  print([1, 2].permutationCount()); // 2.
  print([1, 2, 3].permutationCount()); // 6.
  print([1, 2, 3, 4].permutationCount()); // 24.
}
```

Solution:

```dart
int permutationCount() {
  int count = 1;
  // Linear time O(n), max permutation count size: 2^64 bits.
  for (var i = length; i > 1; i--) {
    count *= i;
  }
  return count;
}
```
