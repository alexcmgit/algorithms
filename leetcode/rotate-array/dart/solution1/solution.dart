class Solution {
  void rotate(List<int> nums, int k) => nums..rotateBy(k);
}

extension<E> on List<E> {
  void rotateBy(int shift) {
    if (isEmpty || length == 1) return;

    shift = shift % length;

    if (shift == 0) return;

    int count = 0;
    int start = 0;

    do {
      int current = start;
      E prev = this[start];

      do {
        int next = (current + shift) % length;
        E temp = this[next];
        this[next] = prev;
        prev = temp;
        current = next;
        count++;
      } while (start != current);

      start = start + 1;
    } while (count < length);
  }
}
