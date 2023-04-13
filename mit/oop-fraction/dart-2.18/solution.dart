import 'dart:math';

class Fraction {
  final int numerator;
  final int denominator;

  const Fraction(this.numerator, this.denominator);

  Fraction operator +(Fraction other) {
    final int top =
        numerator * other.denominator + denominator * other.numerator;
    final int bottom = denominator * other.denominator;
    return Fraction(top, bottom);
  }

  Fraction operator -(Fraction other) {
    final int top =
        numerator * other.denominator - denominator * other.numerator;
    final int bottom = denominator * other.denominator;
    return Fraction(top, bottom);
  }

  Fraction operator *(Fraction other) {
    final int top = numerator * other.numerator;
    final int bottom = denominator * other.denominator;
    return Fraction(top, bottom);
  }

  Fraction operator /(Fraction other) => this * other.inverse();

  Fraction inverse() => Fraction(denominator, numerator);

  bool isEquivalentTo(Fraction other) {
    return simplify() == other.simplify();
  }

  @override
  bool operator ==(Object other) {
    if (other is! Fraction) return false;
    return numerator == other.numerator && denominator == other.denominator;
  }

  @override
  int get hashCode => Object.hashAll(<int>[numerator, denominator]);

  Fraction simplify() {
    final int hcf = _highestCommonFactor(numerator, denominator);
    return Fraction(numerator ~/ hcf, denominator ~/ hcf);
  }

  int _highestCommonFactor(int n, int m) {
    int a = max(n, m);
    int b = min(n, m);

    while (b != 0) {
      final int q = a ~/ b;
      final int r = a - q * b;
      a = b;
      b = r;
    }

    return a;
  }
}
