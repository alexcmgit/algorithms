class Solution {
  String convert(String s, int rows) {
    if (rows == 1) return s;

    final cs = s.split('');
    
    int y = 0;
    int dirY = 1;

    final bufs = List<StringBuffer>.generate(rows, (c) => StringBuffer());

    for (final c in cs) {
      bufs[y].write(c);

      if (y == rows - 1) {
        dirY = -1;
      }
      
      if (y == 0) {
        dirY = 1;
      }

      y = y + dirY;
    }
    
    return bufs.fold('', (acc, e) => acc + e.toString());
  }
}
