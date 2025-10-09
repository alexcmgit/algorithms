void main() {
  final testCases = {
    1: 8,
    9: 8,
    555: 888,
    123456: 820000,
    1101057: 8808050,
  };

  for (final entry in testCases.entries) {
    print('num: ${entry.key} → max difference: ${entry.value}');
  }
}
