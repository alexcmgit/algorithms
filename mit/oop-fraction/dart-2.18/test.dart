import 'dart:io';

import 'solution.dart' as s1;

extension Utils on String {
  List<int> asFraction() => split('/').map(int.parse).toList();
}

extension String2S1Fraction on s1.Fraction {
  String asString() => '$numerator/$denominator';
}

void testSolution1({
  required List<String> commandInputs,
  required List<String> lhsInputs,
  required List<String?> rhsList,
  required List<String?> operatorInputs,
  required List<String> outputs,
}) {
  try {
    for (int i = 0; i < commandInputs.length; i++) {
      final String command = commandInputs[i];

      late s1.Fraction output;
      final String? operator = operatorInputs[i];

      final s1.Fraction lhs = s1.Fraction(
        lhsInputs[i].asFraction()[0],
        lhsInputs[i].asFraction()[1],
      );

      final s1.Fraction? rhs = rhsList[i] != null
          ? s1.Fraction(
              rhsList[i]?.asFraction()[0] ?? 1,
              rhsList[i]?.asFraction()[1] ?? 1,
            )
          : null;

      final s1.Fraction expectedOutput = s1.Fraction(
        outputs[i].asFraction()[0],
        outputs[i].asFraction()[1],
      );

      if (command == 'simplify') {
        output = lhs.simplify();

        if (!lhs.isEquivalentTo(expectedOutput)) {
          throw Exception(
            'The fraction ${lhs.asString()} is equivalent to ${expectedOutput.asString()} but the call [lhs.isEquivalentTo(expectedOutput)] says its not.',
          );
        }
      } else if (command == 'calc') {
        switch (operator) {
          case '+':
            output = lhs + rhs!;
            break;
          case '-':
            output = lhs - rhs!;
            break;
          case '*':
            output = lhs * rhs!;
            break;
          case '/':
            output = lhs / rhs!;
            break;
          default:
            throw Exception(
              'Invalid operation was provided: ${operatorInputs[i]} to [Fraction] class at solution 1.',
            );
        }
      }
      if (expectedOutput != output) {
        throw Exception(
          'Invalid output on solution 1, command was [$command]: expected ${expectedOutput.asString()}, got ${output.asString()}, when input is ${lhs.asString()}${operator ?? ''}${rhs?.asString() ?? ''}.',
        );
      }
    }
    print('✔️ All tests passed for solution 1.');
  } catch (e) {
    throw Exception(
      '❌ Test failed for solution 1, see below logs for details.\n$e',
    );
  }
}

Iterable<List<String>> _parseRawInputOperations(List<String> inputs) sync* {
  for (final String rawInput in inputs) {
    yield rawInput.split(' ');
  }
}

Iterable<String> _parseRawInputCommands(List<String> inputs) sync* {
  for (final List<String> operation in _parseRawInputOperations(inputs)) {
    yield operation[0];
  }
}

Iterable<String> _parseRawInputLhs(List<String> inputs) sync* {
  for (final List<String> operation in _parseRawInputOperations(inputs)) {
    yield operation[1];
  }
}

Iterable<String?> _parseRawInputRhs(List<String> inputs) sync* {
  for (final List<String> operation in _parseRawInputOperations(inputs)) {
    yield operation.length <= 3 + 1 ? operation[3] : null;
  }
}

Iterable<String?> _parseRawInputOperators(List<String> inputs) sync* {
  for (final List<String> operation in _parseRawInputOperations(inputs)) {
    yield operation.length <= 2 + 1 ? operation[2] : null;
  }
}

// Would be so nice if Dart had [test] package as built-in library...
void main(List<String> args) {
  List<String>? arg(int index) {
    return index < args.length ? args[index].split('\n') : null;
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

  final List<String> commandInputs = _parseRawInputCommands(stdin).toList();
  final List<String> lhsInputs = _parseRawInputLhs(stdin).toList();
  final List<String?> rhsInputs = _parseRawInputRhs(stdin).toList();
  final List<String?> operatorInputs = _parseRawInputOperators(stdin).toList();

  testSolution1(
    commandInputs: commandInputs,
    lhsInputs: lhsInputs,
    operatorInputs: operatorInputs,
    outputs: stdout,
    rhsList: rhsInputs,
  );
}
