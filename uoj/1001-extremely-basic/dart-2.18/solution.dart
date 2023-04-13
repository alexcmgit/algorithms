import 'dart:convert';
import 'dart:io';

void main() {
  print('X = ${_getIntLine() + _getIntLine()}');
}

String _getLine() => stdin.readLineSync(encoding: utf8)?.trim() ?? '';

int _getIntLine() => int.tryParse(_getLine())!;
