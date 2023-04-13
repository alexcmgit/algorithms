bool _nand(bool x, bool y) {
  return _not(_and(x, y));
}

bool _or(bool x, bool y) {
  return x | y;
}

bool _and(bool x, bool y) {
  return x & y;
}

bool _xor(bool x, bool y) {
  return x ^ y;
}

bool _not(bool x) {
  return !x;
}

bool _nor(bool x, bool y) {
  return _not(_or(x, y));
}

bool xnor(bool x, bool y) {
  return _not(_nor(x, y));
}

bool door(List<bool> key) {
  bool a = key[0],
      b = key[1],
      c = key[2],
      d = key[3],
      e = key[4],
      f = key[5],
      g = key[6],
      h = key[7],
      i = key[8],
      j = key[9];

  final bool norAB = _nor(a, _not(b));
  final bool orCD = _or(_not(c), d);
  final bool orEF = _and(e, _not(f));
  final bool norCDEF = _nor(orCD, orEF);
  final bool andABCDEF = _and(norAB, norCDEF);
  final bool norGH = _nor(g, h);
  final bool xorHI = _xor(h, i);
  final bool andGHI = _and(norGH, xorHI);
  final bool andIJ = _and(i, j);
  final bool andGHIJ = _and(andGHI, andIJ);
  final bool result = _and(andABCDEF, andGHIJ);

  return result;
}

List<bool> keyFromChars(String chars) {
  chars = chars.toLowerCase();

  return <bool>[
    chars.contains('a'),
    chars.contains('b'),
    chars.contains('c'),
    chars.contains('d'),
    chars.contains('e'),
    chars.contains('f'),
    chars.contains('g'),
    chars.contains('h'),
    chars.contains('i'),
    chars.contains('j'),
  ];
}

void main() {
  print(door(keyFromChars('BCFIJ'))); // True (1).
}
