class Solution {
  String intToRoman(int n, [String c = 'I']) {
    int u = /* ( */ n /* ~/ 1) */ % 10;
    int d = (n ~/ 10) % 10;
    int c = (n ~/ 100) % 10;
    int m = (n ~/ 1000) /* % 10 */ ;

    String mr = switch (m) {
        1 => 'M',
        2 => 'MM',
        3 => 'MMM',
        _ => '',
    };

    String cr = switch (c) {
        1 => 'C',
        2 => 'CC',
        3 => 'CCC',
        4 => 'CD',
        5 => 'D',
        6 => 'DC',
        7 => 'DCC',
        8 => 'DCCC',
        9 => 'CM',
        _ => '',
    };

    String dr = switch (d) {
        1 => 'X',
        2 => 'XX',
        3 => 'XXX',
        4 => 'XL',
        5 => 'L',
        6 => 'LX',
        7 => 'LXX',
        8 => 'LXXX',
        9 => 'XC',
        _ => '',
    };

    String ur = switch (u) {
        1 => 'I',
        2 => 'II',
        3 => 'III',
        4 => 'IV',
        5 => 'V',
        6 => 'VI',
        7 => 'VII',
        8 => 'VIII',
        9 => 'IX',
        _ => '',
    };

    return mr + cr + dr + ur;
  }
}
