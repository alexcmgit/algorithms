void printListNode(ListNode? node) {
  List<int> values = [];
  while (node != null) {
    values.add(node.val);
    node = node.next;
  }
  print(values);
}

// Example usage:

void main() {
  // Test case 1
  ListNode l1_case1 = ListNode(2, ListNode(4, ListNode(3)));
  ListNode l2_case1 = ListNode(5, ListNode(6, ListNode(4)));

  // Test case 2
  ListNode l1_case2 = ListNode(0);
  ListNode l2_case2 = ListNode(0);

  // Test case 3
  ListNode l1_case3 = ListNode(
    9,
    ListNode(
      9,
      ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))),
    ),
  );
  ListNode l2_case3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))));

  Solution solution = Solution();

  printListNode(solution.addTwoNumbers(l1_case1, l2_case1)); // [7,0,8]
  printListNode(solution.addTwoNumbers(l1_case2, l2_case2)); // [0]
  printListNode(
    solution.addTwoNumbers(l1_case3, l2_case3),
  ); // [8,9,9,9,0,0,0,1]
}

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}
