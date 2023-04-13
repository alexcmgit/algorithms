import 'dart:io';
import 'dart:mirrors';

import 'solution.dart' as s1;

typedef Solution = String Function(String n);

// Would be so nice if Dart had [test] package as built-in library...
void main(List<String> args) {
  final List<Solution> solutions = <Solution>[
    (s) => s1.r(s),
    // Import new solutions and add the closure reference here.
  ];

  for (int i = 1; i <= solutions.length; i++) {
    final Solution solution = solutions[i - 1];

    final String solutionFnName =
        '${(MirrorSystem.getName((reflect(solution) as ClosureMirror).function.simpleName))}';
    final String id = '${'$i'.padLeft(2, '0')} [$solutionFnName]';

    try {
      List<String>? arg(int index) {
        try {
          return args[index].split('\n');
        } on RangeError {
          return null;
        }
      }

      if (args.isNotEmpty && args.length != 2) {
        throw Exception(
          'Expecting [args] to be a fixed array of [stdin, stdout] of expected use cases. Got an array of length ${args.length}',
        );
      }

      final File stdinFile =
          File(Platform.script.toFilePath() + '/../../stdin.txt');
      final File stdoutFile =
          File(Platform.script.toFilePath() + '/../../stdout.txt');

      bool notEmpty(String line) => line.isNotEmpty;

      final List<String> stdin =
          arg(0) ?? stdinFile.readAsLinesSync().where(notEmpty).toList();
      final List<String> stdout =
          arg(1) ?? stdoutFile.readAsLinesSync().where(notEmpty).toList();

      final List<String> inputs = stdin.toList();
      final List<String> outputs = stdout.toList();

      for (int i = 0; i < inputs.length; i++) {
        final String input = inputs[i];
        final String expected = outputs[i];
        final String output = solution(input);
        if (output != expected) {
          throw Exception(
            'Invalid output, (input, expected output, output; respectively)\n$input\n$expected\n$output\nfor $solutionFnName($input)',
          );
        }
      }

      print('✅ All tests passed for solution $id.');
    } catch (e) {
      throw Exception(
        '❌ Test failed for solution $id, see below logs for details.\n$e',
      );
    }
  }
}
