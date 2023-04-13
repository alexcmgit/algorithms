import 'dart:convert';
import 'dart:io';
import 'dart:mirrors';

import 'solution.dart' as s1;

typedef Solution = dynamic;

// Would be so nice if Dart had [test] package as built-in library...
void main(List<String> args) {
  final List<Solution> solutions = <Solution>[
    s1.f,
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

      final List<String> stdin =
          arg(0) ?? stdinFile.readAsStringSync().split('\n').toList();
      final List<String> stdout =
          arg(1) ?? stdoutFile.readAsStringSync().split('\n').toList();

      final List<String> inputs = stdin.toList();
      final List<String> outputs = stdout.toList();

      String parseBreakLines(String source) => source
          .replaceAll(r'\n', '\n')
          .replaceAll(r'\t', '\t')
          .replaceAll('EMPTY', '');

      for (int i = 0, o = 0; i < inputs.length - 1; i += 2, o++) {
        final String s = parseBreakLines(inputs[i]);
        final String a = parseBreakLines(inputs[i + 1]);

        final String expected = parseBreakLines(outputs[o]);
        final String output = solution(s, a);

        if (output != expected) {
          throw Exception(
            'Invalid output, expected "$expected" but got "$output" for $solutionFnName($s, $a)',
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
