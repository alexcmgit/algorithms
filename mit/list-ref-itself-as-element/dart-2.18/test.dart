// ignore_for_file: avoid_dynamic_calls

import 'dart:mirrors';

import 'solution1.dart' as s1;
import 'solution2.dart' as s2;

typedef Solution = List<dynamic> Function();

// Would be so nice if Dart had [test] package as built-in library...
void main(List<String> args) {
  final List<Solution> solutions = <Solution>[
    s1.createRecursiveList,
    s2.createRecursiveList,
    // Import new solutions and add the closure reference here.
  ];

  for (int i = 1; i <= solutions.length; i++) {
    final Solution solution = solutions[i - 1];

    final String solutionFnName = MirrorSystem.getName(
      (reflect(solution) as ClosureMirror).function.simpleName,
    );

    final String id = '$i [$solutionFnName]';

    try {
      final List<dynamic> root = solution();
      final List<dynamic> child = root[0] as List<dynamic>;
      final List<dynamic> grandchild =
          root[0][0][0][0][0][0][0][0][0][0][0][0][0] as List<dynamic>;

      // No matter how deep, it must always point to the same object id.
      final List<int> hashes = <int>[
        root.hashCode,
        child.hashCode,
        grandchild.hashCode,
      ];

      if (hashes.toSet().length != 1) {
        throw Exception(
          'This list is not recursive, expected the first element be the list itself, but instead got different object hash codes. $root',
        );
      }

      print('✔️ All tests passed for solution $id.');
    } catch (e) {
      throw Exception(
        '❌ Test failed for solution $id, see below logs for details.\n$e',
      );
    }
  }
}
