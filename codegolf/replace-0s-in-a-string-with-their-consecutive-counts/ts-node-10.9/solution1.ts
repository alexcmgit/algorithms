export default function replaceZerosWithTheirConsecutiveCounts(src: string) {
  return src.replace(/0+/g, (substring: string) => substring.length.toString());
}
