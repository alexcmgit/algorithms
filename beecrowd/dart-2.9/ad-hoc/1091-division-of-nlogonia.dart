import 'dart:convert';
import 'dart:io';

class Point {
  const Point(this.x, this.y);

  final int x;
  final int y;

  bool overline(Point other) => other.x == x || other.y == y;
}

void main() {
  int n;

  while ((n = _getIntLine()) != 0) {
    var input = _getIntListLine();

    final origin = Point(input[0], input[1]);

    for (var i = 0; i < n; i++) {
      input = _getIntListLine();

      final point = Point(input[0], input[1]);

      if (origin.overline(point)) {
        _print('divisa');
      } else {
        _print(origin.y > point.y ? 'S' : 'N');
        _print(origin.x > point.x ? 'O' : 'E');
      }

      _print('\n');
    }
  }
}

void _print(Object object) => stdout.write(object);

String _getLine() =>
    stdin.readLineSync(encoding: Encoding.getByName('utf-8'))?.trim() ?? '';

int _getIntLine() => int.parse(_getLine());

List<int> _getIntListLine() => _getLine().split(' ').map(int.parse).toList();
