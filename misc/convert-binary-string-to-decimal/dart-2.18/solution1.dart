import 'dart:math';

int toDecimal(String binary) {
  final List<String> digits = binary.split('');

  return digits
      .asMap()
      .entries
      .map(
        (MapEntry<int, String> e) =>
            e.value == '0' ? 0 : pow(2, digits.length - 1 - e.key) ~/ 1,
      )
      .reduce((int value, int element) => value + element);
}
