package main

import (
	"fmt"
	"os"
	"path"
	"regexp"
	"runtime"
	"strconv"
)

type Solution func(n int64) int64

func main() {
	// Add your solution right here. Do not forget to append your function to a type to avoid name conflict.
	solutions := [...]Solution{s1{}.MultiplesOf3And5Below, s2{}.MultiplesOf3And5Below}
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
		expected := toInt64(stdout[index])
		input := toInt64(line)

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

func toInt64(source string) int64 {
	value, err := strconv.Atoi(source)

	if err != nil {
		panic(err)
	}

	return int64(value)
}
