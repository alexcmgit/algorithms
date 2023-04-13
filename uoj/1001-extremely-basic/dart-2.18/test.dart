import 'dart:async';
import 'dart:convert';
import 'dart:io';

const String kDartRun = 'dart run';

final String workingDirectory = File(Platform.script.toFilePath()).parent.path;

void _assertSolutionOutput(List<String> output, List<String> expected) {
  for (int i = 0; i < expected.length; i++) {
    if (i > output.length - 1) {
      throw Exception(
        'Expected "${expected[i]}" but got an empty string (end of output).',
      );
    }

    if (output[i] != expected[i]) {
      throw Exception(
        'Found differences on line ${i + 1} (expected, got):\n${expected[i]}\n${output[i]}',
      );
    }

    if (i == expected.length - 1) {
      if (i < output.length - 1) {
        throw Exception(
          'Extra output was idenfied: ${output.sublist(i + 1).join('\n')}.',
        );
      }
    }
  }
}

Future<List<String>> _spawnSolutionProcessAndTakeTheOuput({
  required File file,
  required List<int> input,
}) async {
  final String solutionPath = file.path;

  Future<Process> spawnSolutionProcess() {
    return Process.start(
      kDartRun,
      <String>[solutionPath],
      runInShell: true,
      workingDirectory: workingDirectory,
    );
  }

  final Process process = await spawnSolutionProcess();

  Future<void> feedSolutionStdinProcess() async {
    await process.stdin
        .addStream(Stream<List<int>>.fromIterable(<List<int>>[input]));
    await process.stdin.close();
  }

  await feedSolutionStdinProcess();

  final Future<List<String>> futureOutput = process.stdout
      .transform(const Utf8Decoder())
      .transform(const LineSplitter())
      .toList();

  return futureOutput;
}

Future<void> testSolution({required File file, required String id}) async {
  try {
    final File stdinFile = File('$workingDirectory./../stdin.txt');
    final File stdoutFile = File('$workingDirectory./../stdout.txt');

    final List<String> stdin = await stdinFile
        .openRead()
        .transform(const Utf8Decoder())
        .transform(const LineSplitter())
        .toList();

    final List<String> stdout = await stdoutFile
        .openRead()
        .transform(const Utf8Decoder())
        .transform(const LineSplitter())
        .toList();

    final List<String> input = <String>[];
    int caseId = 0;

    while (stdin.isNotEmpty) {
      input.add(stdin[0]);

      if (input.length == 2) {
        caseId++;

        print('🧪 Spawning process of solution $id on case $caseId.');

        final List<String> expected = <String>[stdout[0]];
        final List<String> output = await _spawnSolutionProcessAndTakeTheOuput(
          file: file,
          input: input.join('\n').codeUnits,
        );

        _assertSolutionOutput(output, expected);

        stdout.removeAt(0);
        input.clear();
      }

      stdin.removeAt(0);
    }

    print('✔️ Successfully tested solution $id.');
  } catch (e) {
    throw Exception(
      '❌ Some tests failed for solution $id: \n$e',
    );
  }
}

Future<void> main() async {
  for (final FileSystemEntity entry in Directory(workingDirectory).listSync()) {
    if (entry is! File) continue;

    final File solution = entry;
    final String name = solution.uri.pathSegments.last;

    if (name.startsWith('solution') && name.endsWith('.dart')) {
      final String id = name.replaceAll('solution', '').replaceAll('.dart', '');
      await testSolution(file: solution, id: id.isEmpty ? '1' : id);
    }
  }
}
