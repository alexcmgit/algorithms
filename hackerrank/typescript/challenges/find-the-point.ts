"use strict";

import { WriteStream, createWriteStream } from "fs";
process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString: string = "";
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on("data", function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on("end", function (): void {
  inputLines = inputString.split("\n");
  inputString = "";

  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

/*
 * Complete the 'findPoint' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER px
 *  2. INTEGER py
 *  3. INTEGER qx
 *  4. INTEGER qy
 */

function findPoint(px: number, py: number, qx: number, qy: number): number[] {
  const dx = qx - px;
  const dy = qy - py;

  return [qx + dx, qy + dy];
}

function main() {
  const ws: WriteStream = createWriteStream(process.env["OUTPUT_PATH"]);

  const n: number = parseInt(readLine().trim(), 10);

  for (let nItr: number = 0; nItr < n; nItr++) {
    const firstMultipleInput: string[] = readLine()
      .replace(/\s+$/g, "")
      .split(" ");

    const px: number = parseInt(firstMultipleInput[0], 10);

    const py: number = parseInt(firstMultipleInput[1], 10);

    const qx: number = parseInt(firstMultipleInput[2], 10);

    const qy: number = parseInt(firstMultipleInput[3], 10);

    const result: number[] = findPoint(px, py, qx, qy);

    ws.write(result.join(" ") + "\n");
  }

  ws.end();
}
