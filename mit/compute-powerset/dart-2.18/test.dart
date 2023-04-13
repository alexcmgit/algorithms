import 'dart:io';
import 'dart:mirrors';

import 'solution.dart' as s1;

typedef Solution = List<List<int>> Function(List<int> n);

// Would be so nice if Dart had [test] package as built-in library...
void main(List<String> args) {
  final List<Solution> solutions = <Solution>[
    s1.powerset,
    // Import new solutions and add the closure reference here.
  ];

  for (int i = 1; i <= solutions.length; i++) {
    final Solution solution = solutions[i - 1];

    final String solutionFnName = MirrorSystem.getName(
      (reflect(solution) as ClosureMirror).function.simpleName,
    );

    final String id = '$i [$solutionFnName]';

    try {
      List<String>? arg(int index) {
        return index >= args.length ? null : args[index].split('\n');
      }

      if (args.isNotEmpty && args.length != 2) {
        throw Exception(
          'Expecting [args] to be a fixed array of [stdin, stdout] of expected use cases. Got an array of length ${args.length}',
        );
      }

      final File stdinFile =
          File('${Platform.script.toFilePath()}/../../stdin.txt');
      final File stdoutFile =
          File('${Platform.script.toFilePath()}/../../stdout.txt');

      bool notEmpty(String line) => line.isNotEmpty;

      String trimLine(String line) => line.trim();

      final List<String> stdin = arg(0) ??
          stdinFile.readAsLinesSync().map(trimLine).where(notEmpty).toList();
      final List<String> stdout = arg(1) ??
          stdoutFile.readAsLinesSync().map(trimLine).where(notEmpty).toList();

      List<int> parseInputList(String input) {
        if (input == '.') return <int>[];

        return input.split(',').map(int.parse).toList();
      }

      List<List<int>> parseOutputList(String input) {
        return input
            .split(' ')
            .map(
              (String e) =>
                  e == '.' ? <int>[] : e.split(',').map(int.parse).toList(),
            )
            .toList();
      }

      final List<List<int>> inputs = stdin.map(parseInputList).toList();
      final List<List<List<int>>> outputs =
          stdout.map(parseOutputList).toList();

      void removeSubsetFrom(List<List<int>> source, List<int> subset) {
        subset.sort((int a, int z) => z - a);

        for (int i = 0; i < source.length; i++) {
          final List<int> set = source[i];
          set.sort((int a, int z) => z - a);

          if (set.length != subset.length) continue;

          bool match = true;

          for (int i = 0; match && i < set.length; i++) {
            if (set[i] != subset[i]) match = false;
          }

          if (match) {
            source.removeAt(i);
            break;
          }
        }
      }

      for (int i = 0; i < inputs.length; i++) {
        final List<int> input = inputs[i];
        final List<List<int>> expected = outputs[i];
        final List<List<int>> output = solution(input);

        for (final List<int> subset in output) {
          removeSubsetFrom(expected, subset);
        }

        if (expected.isNotEmpty) {
          throw Exception(
            'Invalid output, expected $expected but got $output for $solutionFnName($input)',
          );
        }
      }

      print('✔️ All tests passed for solution $id.');
    } catch (e) {
      throw Exception(
        '❌ Test failed for solution $id, see below logs for details.\n$e',
      );
    }
  }
}
