int toDecimal(String binary) {
  final List<String> digits = binary.split('');

  return digits
      .asMap()
      .entries
      .map(
        (MapEntry<int, String> e) =>
            (e.value == '1' ? 1 : 0) * (1 << (digits.length - 1 - e.key)),
      )
      .reduce((int value, int element) => value + element);
}
