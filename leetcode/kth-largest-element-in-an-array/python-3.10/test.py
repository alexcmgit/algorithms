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

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solutions = map(lambda e: (e[1], import_solution(e[0]).Solution().findKthLargest), solutions())
        self.inputs = list(map(lambda line: list(map(int, line.split(' '))), stdin()))
        self.outputs = list(map(int, stdout()))

    def test_solutions(self):
        for id, solution in self.solutions:
            self._assert_solution_expected_output(solution, f'{id}')

    def _assert_solution_expected_output(self, solution, id: str):
        assert callable(solution)

        for i in range(0, len(self.inputs), 2):
            inp_nums = self.inputs[i]
            inp_k = self.inputs[i + 1][0]
            output = solution(inp_nums, inp_k)
            expected = self.outputs[i // 2]
            self.assertEqual(output, expected, f'Expected {expected} but got {output} when calling input ({inp_nums}, {inp_k}) on solution {id}.')

if __name__ == '__main__':
    unittest.main()
