import 'dart:convert';
import 'dart:io';

// (Edit 28/12/2022): I would name this solution [overkill.dart].
void main() {
  const numbersLength = 4;
  const combinationLength = 2;
  final combinations = <List<int>>[];
  for (var i = 0; i < numbersLength; i++) {
    final out = _getIntLine();
    if (combinations.isEmpty || combinations.last.length == combinationLength) {
      combinations.add([out]);
    } else {
      combinations.last.add(out);
    }
  }
  final mults = combinations
      .map((combination) => combination.reduce((ac, element) => ac * element))
      .toList();
  final diff = mults.reduce((ac, element) => ac - element);
  print('DIFERENCA = $diff');
}

String _getLine() {
  final line = stdin.readLineSync(encoding: Encoding.getByName('utf-8'));
  return line.trim();
}

int _getIntLine() => int.parse(_getLine());
