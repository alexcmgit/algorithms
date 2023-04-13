import 'dart:convert';
import 'dart:io';

void main() {
  while (true) {
    final n = _getIntListLine();
    final a = n[0];
    final b = n[1];

    if (a + b == 0) return;

    final carry = _carryOperationsCount(a, b);

    if (carry == 0) {
      print('No carry operation.');
    } else if (carry == 1) {
      print('1 carry operation.');
    } else {
      print('$carry carry operations.');
    }
  }
}

int _carryOperationsCount(int a, int b) {
  var carry = 0;
  var acc = 0;
  var i = a;
  var j = b;

  while (true) {
    final x = i % 10;
    final y = j % 10;

    final sum = x + y + acc;

    acc = sum ~/ 10;

    i ~/= 10;
    j ~/= 10;

    if (acc != 0) carry++;

    if (i + j == 0) return carry;
  }
}

String _getLine() =>
    stdin.readLineSync(encoding: Encoding.getByName('utf-8'))?.trim() ?? '';

List<int> _getIntListLine() => _getLine().split(' ').map(int.parse).toList();
