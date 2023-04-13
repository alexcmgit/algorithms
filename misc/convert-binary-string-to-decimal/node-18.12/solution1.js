module.exports = function toDecimal(binary) {
  return binary
    .split(``)
    .map((d, i, arr) => (d === `0` ? 0 : 2 ** (arr.length - 1 - i)))
    .reduce((total, e) => total + e, 0);
};
