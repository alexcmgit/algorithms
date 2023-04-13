/// Definition for a binary tree node.
class TreeNode {
  final int val;
  final TreeNode? left;
  final TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

/// Note: submit only solution class! The [TreeNode] class is already part of solution when submitting on LeetCode.
class Solution {
  int deepestLeavesSum(TreeNode? root) {
    final List<TreeNode> deepestLeaves = _getDeepestLeaves(root!);

    return deepestLeaves
        .map((TreeNode e) => e.val)
        .reduce((int value, int element) => value + element);
  }

  // This is not being used but this was an implementation helped me
  // to find the "right direction" of the final solution.
  List<TreeNode> _getDepthFreeNodes(TreeNode node, {int depth = 0}) {
    final Map<int, List<TreeNode>> leaves = _getLeaves(node, depth: depth);

    return leaves.values.reduce(
      (List<TreeNode> value, List<TreeNode> element) =>
          <TreeNode>[...value, ...element],
    );
  }

  List<TreeNode> _getDeepestLeaves(TreeNode node, {int depth = 0}) {
    final Map<int, List<TreeNode>> leaves = _getLeaves(node, depth: depth);

    final List<int> levels = leaves.keys.toList()
      ..sort((int a, int z) => z - a);

    final int deepestLevel = levels.first;

    final List<TreeNode> deepestLeaves = leaves[deepestLevel]!;

    return deepestLeaves;
  }

  Map<int, List<TreeNode>> _getLeaves(
    TreeNode node, {
    Map<int, List<TreeNode>> treeByDepth = const <int, List<TreeNode>>{},
    int depth = 0,
  }) {
    // Copy to avoid object reference related bugs.
    Map<int, List<TreeNode>> copy = Map<int, List<TreeNode>>.from(treeByDepth);

    if (node.left == null && node.right == null) {
      copy[depth] = <TreeNode>[...copy[depth] ?? <TreeNode>[], node];
    } else {
      if (node.left != null) {
        copy = _getLeaves(node.left!, treeByDepth: copy, depth: depth + 1);
      }
      if (node.right != null) {
        copy = _getLeaves(node.right!, treeByDepth: copy, depth: depth + 1);
      }
    }

    return copy;
  }
}
