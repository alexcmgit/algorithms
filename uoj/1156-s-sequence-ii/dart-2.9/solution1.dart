// ignore_for_file: parameter_assignments

void main() {
  print(_s().toStringAsFixed(2));
}

// (Edit 28/12/2022): My soul was claiming for code golf and I wasn't aware of that.
double _s([double s = 0.0, int d1 = 1, int d2 = 1]) =>
    d1 <= 39 ? _s(s += d1 / d2, d1 += 2, d2 += d2) : s;
