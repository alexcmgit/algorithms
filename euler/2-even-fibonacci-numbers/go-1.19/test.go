package main

import (
	"fmt"
	"os"
	"path"
	"regexp"
	"runtime"
	"strconv"
)

type Solution func(limit uint64) uint64

func main() {
	solutions := [...]Solution{s1{}.EvenFibonacciNumbersSumUpTo}
	overallOk := true

	for index, solution := range solutions {
		ok, _ := testSolution(solution, uint8(index)+1)
		if !ok {
			overallOk = false
		}
	}

	if overallOk {
		fmt.Println("OK.")
	} else {
		panic("FAIL.")
	}
}

func testSolution(solution Solution, id uint8) (ok bool, errorMessages []string) {
	var stdout = stdoutLines()

	ok = true

	for index, line := range stdinLines() {
		expected := toUint64(stdout[index])
		input := toUint64(line)

		output := solution(input)

		fmt.Print("Ran | Solution [", id, "] | Case [", index+1, "]")

		if output != expected {
			ok = false

			reason := "  - Expecting " + fmt.Sprint(expected) + " but got " + fmt.Sprint(output) + " on case " + fmt.Sprint(index+1) + " on solution " + fmt.Sprint(id)

			fmt.Println(" (FAIL)")
			fmt.Println(reason)

			errorMessages = append(errorMessages, reason)
		} else {
			fmt.Println(" (OK)")
		}
	}

	fmt.Println("------------------------------------")

	return
}

func currentFile() string {
	_, filepath, _, ok := runtime.Caller(0)

	if !ok {
		panic("No caller.")
	}

	return filepath
}

func currentDir() string {
	return path.Dir(currentFile())
}

func readStd(filename string) string {
	bytes, err := os.ReadFile(path.Join(currentDir(), "..", filename))

	if err != nil {
		panic(err)
	}

	return string(bytes)
}

func readStdin() string {
	return readStd("stdin.txt")
}

func readStdout() string {
	return readStd("stdout.txt")
}

func splitByNewLine(source string) []string {
	return regexp.MustCompile("\r?\n").Split(source, -1)
}

func stdinLines() []string {
	return splitByNewLine(readStdin())
}

func stdoutLines() []string {
	return splitByNewLine(readStdout())
}

func toUint64(source string) uint64 {
	value, err := strconv.Atoi(source)

	if err != nil {
		panic(err)
	}

	return uint64(value)
}
