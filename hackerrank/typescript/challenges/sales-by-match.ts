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
 * Complete the 'sockMerchant' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY ar
 */

type HashMap = {
  [k: number]: number[];
};

function sockMerchant(n: number, values: number[]): number {
  const waitHashMap: HashMap = {};
  const pairMatrix: number[][] = [];

  function waitList(value: number): number[] {
    return waitHashMap[value] || (waitHashMap[value] = []);
  }

  function popWaitValue(value: number): void {
    waitList(value).pop();
  }

  function pushWaitValue(value: number): void {
    waitList(value).push(value);
  }

  function hasPair(value: number): boolean {
    return waitList(value).length > 0;
  }

  function addPair(value: number) {
    pairMatrix.push([value, value]);

    popWaitValue(value);
  }

  for (const value of values) {
    if (hasPair(value)) {
      addPair(value);
    } else {
      pushWaitValue(value);
    }
  }

  return pairMatrix.length;
}

function main(): void {
  const ws: WriteStream = createWriteStream(process.env["OUTPUT_PATH"]);

  const n: number = parseInt(readLine().trim(), 10);

  const ar: number[] = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arTemp) => parseInt(arTemp, 10));

  const result: number = sockMerchant(n, ar);

  ws.write(result + "\n");

  ws.end();
}
