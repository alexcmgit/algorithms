import 'dart:convert';
import 'dart:io';

void main() {
  var count = 1;
  var n = 0;

  for (; (n = _getIntLine()) != null; count++) {
    final output = StringBuffer();

    var c = 0;
    var i = 0;

    do {
      var j = 0;
      do {
        output.write('$i ');
        j++;
        c++;
      } while (j < i);
      i++;
    } while (i <= n);

    final displayCount = c == 1 ? '$c numero' : '$c numeros';

    print('Caso $count: $displayCount\n${'$output'.trim()}\n');
  }
}

String _getLine() =>
    stdin.readLineSync(encoding: Encoding.getByName('utf-8')) ?? '';

int _getIntLine() => int.tryParse(_getLine());
