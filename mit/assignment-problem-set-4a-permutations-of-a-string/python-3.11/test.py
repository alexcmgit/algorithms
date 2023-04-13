import os
import unittest
from typing import Any
import importlib

ROOT = os.path.dirname(os.path.realpath(__file__))

def solutions() -> list[tuple[str, int]]:
    modules = []
    for file in os.listdir(ROOT):
        if file.startswith('solution') and file.endswith('.py'):
            id = file[len('solution'):-len('.py')]
            modules.append((file[:-len('.py')], int(id) if len(id) > 0 else 1))
    return sorted(modules, key=lambda e: e[1])

def stdin() -> list[str]:
    with open(os.path.realpath(os.path.join(ROOT, '..', 'stdin.txt')), 'r') as f:
        return list(filter(lambda e: len(e) > 0, map(lambda e: e.strip(), f.readlines())))

def stdout() -> list[str]:
    with open(os.path.realpath(os.path.join(ROOT, '..', 'stdout.txt')), 'r') as f:
        return list(filter(lambda e: len(e) > 0, map(lambda e: e.strip(), f.readlines())))

def import_solution(solution: str) -> Any:
    return importlib.import_module(solution)

class BaseSolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stdin_line = stdin()
        self.stdout_lines = stdout()
        self.solutions = solutions()

    def test_solutions(self):
        for solution, id in self.solutions:
            self._test_get_permutations(import_solution(solution), id)

    def _test_get_permutations(self, solution, id: int):
        for i, stdin in enumerate(self.stdin_line):
            print(f'Solution {id} | Case {i + 1}')
            stdout = self.stdout_lines[i]
            out = sorted(solution.get_permutations(stdin))
            exp = sorted(stdout.split(' '))
            self.assertListEqual(out, exp)
        print('-' * 20)

if __name__ == '__main__':
    unittest.main()


