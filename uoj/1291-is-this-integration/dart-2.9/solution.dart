import 'dart:convert';
import 'dart:io';

import 'dart:math';

void main() {
  double n;

  while ((n = _getDoubleLine()) != null) {
    final area = n * n;

    const oneTwelfth = pi / 12;
    const oneFourth = pi / 4;

    /// All formulas are fractioned (relative to 1)
    /// Area of a equilateral triangle = sqrt(3) / 4 (because side equals to 1)
    /// Area of a twelfth part of a circle = pi / 12 (because the radius equals to 1)
    /// Same for the one fourth part of a circle
    final fexternal = 1 - oneTwelfth * 2 - sqrt(3) / 4;
    final finternal = 1 - oneFourth - fexternal * 2;
    final fcenter = 1 - 4 * finternal - 4 * fexternal;

    /// Apply all fractioned values to the given area of the input value `n` (side of the shape)
    final external = area * fexternal * 4;
    final internal = area * finternal * 4;
    final center = area * fcenter;

    print('${_fixed(center)} ${_fixed(internal)} ${_fixed(external)}');
  }
}

String _fixed(double n) => n.toStringAsFixed(3);

String _getLine() =>
    stdin.readLineSync(encoding: Encoding.getByName('utf-8'))?.trim() ?? '';

double _getDoubleLine() => double.tryParse(_getLine());
