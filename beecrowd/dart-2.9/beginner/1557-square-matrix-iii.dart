import 'dart:convert';
import 'dart:io';

import 'dart:math';

void main() {
  int n;

  while ((n = _getIntLine()) != 0) {
    final t = '${pow(2, n + n - 2)}'.length;

    for (var i = 0; i < n; i++) {
      for (var j = 0; j < n; j++) {
        final current = pow(2, i + j);

        _print('$current'.padLeft(j == 0 ? t : t + 1));
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
