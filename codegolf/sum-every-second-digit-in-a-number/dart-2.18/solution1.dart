int sumEverySecondDigitInANumber(int n) {
  return '$n'
      .split('')
      .asMap()
      .entries
      .where((MapEntry<int, String> e) => e.key.isOdd)
      .map((MapEntry<int, String> e) => int.parse(e.value))
      .reduce((value, element) => value + element);
}
