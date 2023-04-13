import BigNumber from "bignumber.js";

// Tried with some smaller numbers and failed on sqrt(17) or sqrt(20).
BigNumber.config({
  DECIMAL_PLACES: 8000,
});

const DEFAULT_PRECISION = new BigNumber(100);

function compute(r, i) {
  const lhs = new BigNumber(
    r.pow(2).dividedBy(new BigNumber(4 * i + 1))
  ).decimalPlaces(0, BigNumber.ROUND_FLOOR);
  const rhs = new BigNumber(
    r.pow(2).dividedBy(new BigNumber(4 * i + 3))
  ).decimalPlaces(0, BigNumber.ROUND_FLOOR);
  return lhs.minus(rhs);
}

function summation(r, precision = DEFAULT_PRECISION) {
  let i = new BigNumber(0);
  let sum = new BigNumber(0);
  while (i.isLessThan(precision)) {
    sum = sum.plus(compute(r, i));
    i = i.plus(new BigNumber(1));
  }
  return sum;
}

export default function points(r, precision = DEFAULT_PRECISION) {
  return 1 + 4 * summation(r, precision);
}
