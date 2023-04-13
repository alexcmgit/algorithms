String replaceZerosWithTheirConsecutiveCounts(String src) {
  return src.replaceAllMapped(
    RegExp('0+'),
    (Match match) => '${match.end - match.start}',
  );
}
