const fs = require("fs");
const path = require("path");

const EXT = `.js`;

function readStd(filename) {
  return fs.readFileSync(path.resolve(path.join(__dirname, `..`, filename)), {
    encoding: `utf-8`,
  });
}

function readStdin() {
  return readStd(`stdin.txt`);
}

function readStdout() {
  return readStd(`stdout.txt`);
}

const stdin = readStdin();

const stdout = readStdout();

const solutions = fs
  .readdirSync(__dirname)
  .filter(
    (filename) => filename.startsWith(`solution`) && filename.endsWith(EXT)
  );

function lineNotEmpty(line) {
  return line.trim().length > 0;
}

function testSolution(solution, id) {
  const inputs = stdin.split(`\n`).filter(lineNotEmpty);
  const outputs = stdout.split(`\n`).filter(lineNotEmpty).map(Number);

  for (let i = 0; i < inputs.length; i++) {
    const input = inputs[i];
    const expected = outputs[i];
    const output = solution(input);

    if (expected !== output) {
      throw Error(
        `Invalid output, (current output, expected, input; respectively):\n${output}\n${expected}\n${input}`
      );
    }
  }
}

if (solutions.length === 0) {
  console.log(`⚠️ No solutions were found in ${__dirname}.`);
}

for (const filename of solutions) {
  const taggedId = filename.replace(`solution`, ``).replace(EXT, ``);

  const id = taggedId.length > 0 ? taggedId : "1";

  const solution = require(path.join(__dirname, filename));

  try {
    testSolution(solution, id);
    console.log(
      `✔️ Ran test suite for solution ${id} [${
        solution.name || "Anonymous Function"
      }].`
    );
  } catch (e) {
    throw Error(
      `❌ Test suite failed for solution ${id} [${solution.name}]:\n${e}`
    );
  }
}
