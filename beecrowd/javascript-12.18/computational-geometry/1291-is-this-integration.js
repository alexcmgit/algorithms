const input = require("fs").readFileSync("/dev/stdin", "utf8");
const lines = input.split("\n");

const fixed = (n) => n.toFixed(3);

for (const line of lines) {
  if (!line) break;

  const n = Number(line);

  const area = n * n;

  const oneTwelfth = Math.PI / 12;
  const oneFourth = Math.PI / 4;

  /**
   * All formulas are fractioned (relative to 1)
   * Area of a equilateral triangle = sqrt(3) / 4 (because side equals to 1)
   * Area of a twelfth part of a circle = pi / 12 (because the radius equals to 1)
   * Same for the one fourth part of a circle
   */
  const fexternal = 1 - oneTwelfth * 2 - Math.sqrt(3) / 4;
  const finternal = 1 - oneFourth - fexternal * 2;
  const fcenter = 1 - 4 * finternal - 4 * fexternal;

  /**
   * Apply all fractioned values to the given area of the input value `n` (side of the shape)
   */
  const external = area * fexternal * 4;
  const internal = area * finternal * 4;
  const center = area * fcenter;

  console.log(`${fixed(center)} ${fixed(internal)} ${fixed(external)}`);
}
