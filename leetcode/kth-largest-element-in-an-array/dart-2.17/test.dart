import 'dart:io';
import 'dart:mirrors';

import 'solution.dart' as s1;

typedef Solution = int Function(List<int> nums, int k);

// Would be so nice if Dart had [test] package as built-in library...
void main(List<String> args) {
  final List<Solution> solutions = <Solution>[
    s1.Solution().findKthLargest,
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

      final List<String> stdin =
          arg(0) ?? stdinFile.readAsLinesSync().where(notEmpty).toList();
      final List<String> stdout =
          arg(1) ?? stdoutFile.readAsLinesSync().where(notEmpty).toList();

      final List<List<int>> inputs = stdin
          .map((String line) => line.split(' ').map(int.parse).toList())
          .toList();

      final List<int> outputs = stdout.map(int.parse).toList();

      for (int i = 0; i < inputs.length; i += 2) {
        final List<int> inputNums = inputs[i];
        final int inputK = inputs[i + 1].first;
        final int expected = outputs[i ~/ 2];
        final int output = solution(inputNums, inputK);
        if (output != expected) {
          throw Exception(
            'Invalid output, expected $expected but got $output for $solutionFnName($inputNums, $inputK)',
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
