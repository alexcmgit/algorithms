function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
  const greatest = new Array(candies.length).fill(false);

  let g = 0;
  for (const c of candies) if (c > g) g = c;
  return candies.map((e) => e + extraCandies >= g);
}
