import 'dart:convert';
import 'dart:io';

import 'dart:math';

void main() {
  List<double> m;

  while ((m = _getDoubleListLine()) != null) {
    final a = m[0];
    final b = m[1];
    final c = m[2];
    final s = (a + b + c) / 2;

    /// Trust the formulas https://math.stackexchange.com/questions/396085/how-to-find-area-of-triangle-from-its-medians
    final result = 4 / 3 * sqrt(s * (s - a) * (s - b) * (s - c));

    final area = result.isNaN || result == 0.0 ? -1 : result;

    print(area.toStringAsFixed(3));
  }
}

String _getLine() =>
    stdin.readLineSync(encoding: Encoding.getByName('utf-8'))?.trim() ?? '';

List<double> _getDoubleListLine() {
  final line = _getLine();

  if (line.isEmpty) return null;

  return line.split(' ').map(double.parse).toList();
}
