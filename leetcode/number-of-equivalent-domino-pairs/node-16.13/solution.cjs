/**
 * @param {number[][]} dominoes
 * @return {number}
 */
const numEquivDominoPairs = function (dominoes) {
  let total = 0;

  for (let i = 0; i < dominoes.length; i++) {
    for (let j = i + 1; j < dominoes.length; j++) {
      const [a, b] = [dominoes[i], dominoes[j]];
      const c1 = a[0] === b[0] && a[1] === b[1];
      const c2 = a[0] === b[1] && a[1] === b[0];

      if (c1 || c2) {
        total++;
      }
    }
  }

  return total;
};

module.exports = numEquivDominoPairs