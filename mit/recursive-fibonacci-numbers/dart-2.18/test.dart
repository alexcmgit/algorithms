import 'dart:io';
import 'dart:mirrors';

import 'solution1.dart' as s1;
import 'solution2.dart' as s2;

typedef Solution = int Function(int n);

// Would be so nice if Dart had [test] package as built-in library...
void main(List<String> args) {
  final List<Solution> solutions = <Solution>[
    s1.fib,
    s2.fib,
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
        return index < args.length ? args[index].split('\n') : null;
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

      final List<int> inputs = stdin.map(int.parse).toList();
      final List<int> outputs = stdout.map(int.parse).toList();

      for (int i = 0; i < inputs.length; i++) {
        final int input = inputs[i];
        final int expected = outputs[i];
        final int output = solution(input);
        if (output != expected) {
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
