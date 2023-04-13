module.exports = function toDecimal(binary) {
  return binary
    .split(``)
    .map((d, i, arr) => (d === `1`) * (1 << (arr.length - 1 - i)))
    .reduce((total, e) => total + e, 0);
};
