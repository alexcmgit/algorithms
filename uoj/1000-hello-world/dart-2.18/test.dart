import 'dart:async';
import 'dart:convert';
import 'dart:io';

const String kDartRun = 'dart run';

final String workingDirectory = File(Platform.script.toFilePath()).parent.path;

Future<void> testSolution({required File file, required String id}) async {
  try {
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
      final File stdinFile = File('$workingDirectory./../stdin.txt');

      await process.stdin.addStream(stdinFile.openRead());
      await process.stdin.close();
    }

    await feedSolutionStdinProcess();

    final Future<List<String>> futureOutput = process.stdout
        .transform(const Utf8Decoder())
        .transform(const LineSplitter())
        .toList();

    final File stdoutFile = File('$workingDirectory./../stdout.txt');

    final List<String> stdout = await stdoutFile
        .openRead()
        .transform(const Utf8Decoder())
        .transform(const LineSplitter())
        .toList();

    final List<String> output = await futureOutput;

    for (int i = 0; i < stdout.length; i++) {
      if (i > output.length - 1) {
        throw Exception(
          'Expected "${stdout[i]}" but got an empty string (end of output).',
        );
      }

      if (output[i] != stdout[i]) {
        throw Exception(
          'Found differences on line ${i + 1} (expected, got):\n${stdout[i]}\n${output[i]}',
        );
      }

      if (i == stdout.length - 1) {
        if (i < output.length - 1) {
          throw Exception(
            'Extra output was idenfied: ${output.sublist(i + 1).join('\n')}.',
          );
        }
      }
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
