extension on int {
  int toggle() => this == 1 ? 0 : 1;
}

T t<T>(T Function() fn, T or) {
  try {
    return fn();
  } on RangeError {
    return or;
  }
}

List<int> lightCandles(List<int> candles, {List<int> path = const <int>[]}) {
  if (candles.length == 1 && candles[0] == 1) return path;
  if (candles.length == 1 && candles[0] == 0) return path;
  final int i = candles.indexOf(0);

  print(candles);

  if (i == -1) return path;

  final int offset = i - 1 == 0 ? 1 : 0;

  t(() => candles[i + offset] = candles[i + offset].toggle(), null);
  t(() => candles[i - 1 + offset] = candles[i - 1 + offset].toggle(), null);
  t(() => candles[i - 2 + offset] = candles[i - 2 + offset].toggle(), null);

  return lightCandles(candles, path: path + [i - 1 + offset]);
}
