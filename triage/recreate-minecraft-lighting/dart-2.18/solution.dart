import 'dart:io';

extension ListExt<E> on List<E> {
  E? get(int index) {
    if (index < 0 || index >= length) return null;
    return this[index];
  }

  List<E> set(int index, E value) {
    if (index >= 0 && index < length) {
      this[index] = value;
    }

    return this;
  }
}

extension Matrix2 on List<List<int>> {
  bool _isLower(int? n, [int compare = 0]) =>
      n != null && n >= 0 && n < compare;

  List<List<int>> applyMinecraftLuminance({
    List<List<int>>? copy,
    int x = 0,
    int y = 0,
  }) {
    final List<List<int>> matrix = copy ??
        <List<int>>[
          ...map((List<int> e) => <int>[...e])
        ];

    if (x == matrix.length - 1 && y == matrix.length - 1) return matrix;

    final List<int>? row = matrix.get(y);
    final int? col = row?.get(x);

    if (col == null) {
      return applyMinecraftLuminance(copy: matrix, y: y + 1);
    }

    if (col == 0) {
      return applyMinecraftLuminance(copy: matrix, x: x + 1, y: y);
    }

    final int prev = x - 1;
    final int next = x + 1;

    final int light = col - 1;

    final int? left = row?.get(prev);
    final int? right = row?.get(next);

    final List<int>? above = matrix.get(y - 1);
    final List<int>? below = matrix.get(y + 1);

    final int? top = above?.get(x);
    final int? bottom = below?.get(x);

    if (_isLower(right, light)) row?.set(next, light);

    if (_isLower(bottom, light)) below?.set(x, light);

    if (_isLower(top, light)) {
      above!.set(x, light);

      return applyMinecraftLuminance(copy: matrix, x: x, y: y - 1);
    }

    if (_isLower(left, light)) {
      row?.set(prev, light);

      return applyMinecraftLuminance(copy: matrix, x: prev, y: y);
    }

    return applyMinecraftLuminance(copy: matrix, x: next, y: y);
  }
}

List<List<int>> recreateMinecraftLightning(List<List<int>> matrix) {
  return matrix.applyMinecraftLuminance();
}

void main() {
  final List<List<List<int>>> cases = <List<List<int>>>[
    <List<int>>[
      <int>[0, 0, 4, 0],
      <int>[0, 0, 0, 0],
      <int>[0, 2, 0, 0],
      <int>[0, 0, 0, 0]
    ],
    <List<int>>[
      <int>[2, 0, 0, 3],
      <int>[0, 0, 0, 0],
      <int>[0, 0, 0, 0],
      <int>[0, 0, 0, 0]
    ],
    <List<int>>[
      <int>[2, 0, 0, 3],
      <int>[0, 0, 0, 0],
      <int>[0, 0, 15, 0],
      <int>[10, 0, 0, 0]
    ],
  ];

  for (final List<List<int>> input in cases) {
    final List<List<int>> output = input.applyMinecraftLuminance();

    _print(output);
  }
}

void _print(List<List<int>> matrix) {
  for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
      stdout.write('${matrix[i][j]} ');
    }

    stdout.write('\n');
  }
}
