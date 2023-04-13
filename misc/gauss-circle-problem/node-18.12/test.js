import fs from "fs";
import path from "path";
import { fileURLToPath } from "node:url";
import { EOL as HOST_PLATFORM_EOL } from "node:os";
import BigNumber from "bignumber.js";

// Each tester should import and test it's own implementation.
// It takes 3 args: (stdin, stdout, id) which are respectively:
// - An string[] of lines of [stdin.txt] file.
// - An string[] of lines of [stdout.txt] file.
// - An numeric string that can be used to identify the solution (it is defined by the function name digit idenfiers).
const testers = [testSolution1];

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const EOL = /\r\n|\r|\n/;

const stdin = readStdin();
const stdout = readStdout();

if (testers.length === 0) {
  console.log(`⚠️ No solutions were found in ${__dirname}.`);
} else {
  await runTests(testers);
}

async function runTests(testers) {
  for (let i = 0; i < testers.length; i++) {
    const test = testers[i];

    const id = test.name.replace(/\D+/g, "");

    try {
      await test(stdin, stdout, id);

      console.log(
        `✔️ Ran test suite for solution ${id} [${
          test.name || "Anonymous Function"
        }].`
      );
    } catch (e) {
      throw Error(
        `❌ Test suite failed for solution ${id} [${test.name}]:\n${e}`
      );
    }
  }
}

async function testSolution1(stdin, stdout, id) {
  const { default: points } = await import("./solution.js");

  for (let i = 0; i < stdin.length; i++) {
    const line = stdin[i];
    const expected = Number(stdout[i]);

    let r = undefined;

    if (line.startsWith(`sqrt`)) {
      const n = Number(line.split(` `)[1]);
      r = BigNumber(n).sqrt();
    } else {
      const n = Number(line);
      r = BigNumber(n);
    }

    console.log(`Running case ${i + 1} on solution ${id}.`);

    const output = points(r);

    if (output !== expected) {
      throw Error(
        `Error on solution ${id}: expecting ${expected} but got ${output} on solution ${id} when input is ${r}.`
      );
    }
  }
}

function readStd(filename) {
  return fs.readFileSync(path.resolve(__dirname, path.join(`..`, filename)), {
    encoding: `utf-8`,
  });
}

function readStdin() {
  return readStd(`stdin.txt`).split(EOL);
}

function readStdout() {
  return readStd(`stdout.txt`).split(EOL);
}
