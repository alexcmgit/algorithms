import 'dart:convert';
import 'dart:io';

import 'dart:math';

void main() {
  int n;

  while ((n = _getIntLine()) != 0) {
    for (var i = 0; i < n; i++) {
      for (var j = 0; j < n; j++) {
        final current = (i - j).abs();
        _print('${current + 1}'.padLeft(j == 0 ? 3 : 4));
      }
      _print('\n');
    }
    _print('\n');
  }
}

void _print(Object object) => stdout.write(object);

String _getLine() =>
    stdin.readLineSync(encoding: Encoding.getByName('utf-8'))?.trim() ?? '';

int _getIntLine() => int.parse(_getLine());
