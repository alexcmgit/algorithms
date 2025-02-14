function canPlaceFlowers(flowerbed: number[], n: number): boolean {
  let f = 0;
  for (let i = 0; i < flowerbed.length; i++) {
    if (flowerbed[i]) continue;
    if (flowerbed[i - 1] !== 1 && flowerbed[i + 1] !== 1) {
      flowerbed[i] = 1;
      f++;
    }
    if (f >= n) return true;
  }
  return f >= n;
}
