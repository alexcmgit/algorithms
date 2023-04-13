bool comp(List<int> a1, List<int> a2) {
  if (a1.length != a2.length) return false;

  for (var i = 0; i < a1.length; i++) {
    /// Find the match index where element is squared
    final match = a2.indexOf(a1[i] * a1[i]);

    /// If has no match, then the arrays are not the "same"
    if (match == -1) {
      return false;
    } else {
      /// Otherwise, we use this match to mark the index as used
      a2[match] = -1;
    }
  }

  return true;
}
