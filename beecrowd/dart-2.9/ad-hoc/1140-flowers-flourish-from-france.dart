import 'dart:convert';
import 'dart:io';

void main() {
  String n;

  while ((n = _getLine()) != '*') {
    final first = n[0];
    final regex = RegExp('^$first', caseSensitive: false);

    if (n.split(' ').every((e) => regex.hasMatch(e))) {
      print('Y');
    } else {
      print('N');
    }
  }
}

String _getLine() =>
    stdin.readLineSync(encoding: Encoding.getByName('utf-8'))?.trim() ?? '';
