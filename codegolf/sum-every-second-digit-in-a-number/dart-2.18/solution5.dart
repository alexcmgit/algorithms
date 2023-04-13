int sumEverySecondDigitInANumber(int n) {
  return <int>[for (int i = 1; i < '$n'.length; i += 2) int.parse('$n'[i])]
      .reduce((value, element) => value + element);
}
