import 'dart:math';

class Vector2 {
  final int x;
  final int y;
  const Vector2(this.x, this.y);

  static const Vector2 zero = Vector2(0, 0);
}

class Rect2 {
  final Vector2 a;
  final Vector2 b;

  const Rect2(this.a, this.b);
  static const Rect2 zero = Rect2(Vector2.zero, Vector2.zero);

  int get width => x2 - x1;
  int get height => y2 - y1;

  int get x1 => min(a.x, b.x);
  int get x2 => max(a.x, b.x);
  int get y1 => min(a.y, b.y);
  int get y2 => max(a.y, b.y);

  int get area => width * height;

  bool containsPoint(Point<double> point) {
    if (point.x >= x1 && point.x <= x2) {
      if (point.y >= y1 && point.y <= y2) {
        return true;
      }
    }
    return false;
  }

  Rect2 overlap(Rect2 other) {
    final bool hasNoOverlapingX = other.x1 > x2 || other.x2 < x1;
    final bool hasNoOverlapingY = other.y1 > y2 || other.y2 < y1;

    if (hasNoOverlapingX || hasNoOverlapingY) {
      return Rect2.zero;
    }

    final int notOverlapingX1 = max(0, other.x1 - x1);
    final int notOverlapingX2 = max(0, x2 - other.x2);

    final int notOverlapingY1 = max(0, other.y1 - y1);
    final int notOverlapingY2 = max(0, y2 - other.y2);

    return Rect2(
      Vector2(x1 + notOverlapingX1, y1 + notOverlapingY1),
      Vector2(x2 - notOverlapingX2, y2 - notOverlapingY2),
    );
  }
}

// A pretty good solution would be something that can get the overlap
// area even if the rect itself is inside another rect.
// But this solution only detects an overlap
// if a given rect is inside it someway, not inside of some other rect.
class Solution {
  int computeArea(
    int ax1,
    int ay1,
    int ax2,
    int ay2,
    int bx1,
    int by1,
    int bx2,
    int by2,
  ) {
    final Rect2 a = Rect2(
      Vector2(ax1, ay1),
      Vector2(ax2, ay2),
    );
    final Rect2 b = Rect2(
      Vector2(bx1, by1),
      Vector2(bx2, by2),
    );

    final Rect2 overlapA = a.overlap(b);
    final Rect2 overlapB = b.overlap(a);

    final Rect2 overlap = overlapA == Rect2.zero ? overlapB : overlapA;

    return a.area + b.area - overlap.area;
  }
}
