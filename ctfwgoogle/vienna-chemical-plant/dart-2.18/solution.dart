const List<int> kObfuscated = [
  52037,
  52077,
  52077,
  52066,
  52046,
  52063,
  52081,
  52081,
  52085,
  52077,
  52080,
  52066,
];

const int kBase = 51966;

String which(int n) => String.fromCharCode(n - kBase);
String password(List<int> obfuscated) => obfuscated.map(which).toList().join();

void main() => print(password(kObfuscated));
