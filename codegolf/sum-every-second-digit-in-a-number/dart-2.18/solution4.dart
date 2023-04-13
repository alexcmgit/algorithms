int sumEverySecondDigitInANumber(int n) {
  final String k = '$n'.padRight(2, '0');

  if (k.length == 2) return int.parse(k[1]);

  return int.parse(k[1]) +
      sumEverySecondDigitInANumber(int.parse(k.substring(2)));
}
