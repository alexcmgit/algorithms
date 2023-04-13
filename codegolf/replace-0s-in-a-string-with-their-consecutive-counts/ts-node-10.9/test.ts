import fs from "fs";
import path from "path";

function readStd(filename: string) {
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

const stdin: string = readStdin();

const stdout: string = readStdout();

const solutions: string[] = fs.readdirSync(__dirname);

type Solution = (src: string) => string;

for (const filename of solutions) {
  if (filename.startsWith(`solution`) && filename.endsWith(`.ts`)) {
    const taggedId: string = filename
      .replace(`solution`, ``)
      .replace(`.ts`, ``);

    const id: string = taggedId.length > 0 ? taggedId : "1";

    const solution: Solution = require(path.join(__dirname, filename)).default;

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
}

function lineNotEmpty(line: string) {
  return line.trim().length > 0;
}

function testSolution(solution: Solution, id: string): void {
  const inputs: string[] = stdin.split(`\n`).filter(lineNotEmpty);
  const outputs: string[] = stdout.split(`\n`).filter(lineNotEmpty);

  for (let i: number = 0; i < inputs.length; i++) {
    const input = inputs[i];
    const expected = outputs[i];
    const output: string = solution(input);

    if (expected !== output) {
      throw Error(
        `Invalid output, (current output, expected, input; respectively):\n${output}\n${expected}\n${input}`
      );
    }
  }
}
