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
 * Complete the 'jumpingOnClouds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY c as parameter.
 */

function jumpingOnClouds(c: number[]): number {
  let jumps = 0;

  for (let i = 0; i < c.length - 1; i += c[i + 2] === 1 ? 1 : 2, jumps++) {}

  return jumps;
}

function main() {
  const ws: WriteStream = createWriteStream(process.env["OUTPUT_PATH"]);

  const n: number = parseInt(readLine().trim(), 10);

  const c: number[] = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((cTemp) => parseInt(cTemp, 10));

  const result: number = jumpingOnClouds(c);

  ws.write(result + "\n");

  ws.end();
}
