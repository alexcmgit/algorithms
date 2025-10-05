/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  ListNode? addTwoNumbers(ListNode? l1, ListNode? l2) {
    ListNode? rtemp;
    ListNode? rhead;
    int remaining = 0;

    do {
      final d1 = l1?.val ?? 0;
      final d2 = l2?.val ?? 0;

      l1 = l1?.next;
      l2 = l2?.next;

      final dsum = d1 + d2 + remaining;

      final (dsumd1, dsumd2) = getDigitsOf(dsum);

      late int dsumdres;
      late int dsumdrem;

      if (dsumd2 != null) {
        dsumdres = dsumd2;
        dsumdrem = dsumd1!;
      } else {
        dsumdres = dsumd1!;
        dsumdrem = 0;
      }

      if (rtemp == null) {
        rhead = ListNode(dsumdres, null);
        rtemp = rhead;
      } else {
        rtemp.next = ListNode(dsumdres, null);
        rtemp = rtemp.next;
      }

      remaining = dsumdrem;
    } while (l1 != null || l2 != null || remaining > 0);
    

    return rhead;
  }

  (int?, int?) getDigitsOf(int n) {
    if (n > 9) {
        return (n ~/ 10, n % 10);
    }
    return (n, null);
  }
}
