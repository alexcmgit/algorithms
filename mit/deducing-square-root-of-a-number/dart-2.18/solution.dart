import 'dart:math';

const double _kPrecision = 4.0;

double deduceSquareRootOf(double x, {double? guess}) {
  final double g = guess ?? x / 4;
  final double r = g * g;

  final double margin = pow(10, _kPrecision) / 1;

  if ((r - x).abs() <= 1 / margin) {
    // You can return g directly if you wanna remove any extra decimal place.
    return ((g * margin) ~/ 1) / margin;
  }

  return deduceSquareRootOf(x, guess: (g + x / g) / 2);
}
