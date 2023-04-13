const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n').map(Number);
const numbers = lines.slice(0, lines.length - 1);

const count = numbers.reduce((acc, current) => acc + (current % 2 ? 0 : 1), 0);

console.log(count + " valores pares");
