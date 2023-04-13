import os
import unittest

ROOT = os.path.dirname(os.path.realpath(__file__))

def solutions():
    modules = []
    for file in os.listdir(ROOT):
        if file.startswith('solution') and file.endswith('.py'):
            id = file[len('solution'):-len('.py')]
            modules.append((file[:-len('.py')], int(id) if len(id) > 0 else 1))
    return sorted(modules, key=lambda e: e[1])

def stdin():
    with open(os.path.realpath(os.path.join(ROOT, '..', 'stdin.txt')), 'r') as f:
        return filter(lambda e: len(e) > 0, map(lambda e: e.strip(), f.readlines()))

def stdout():
    with open(os.path.realpath(os.path.join(ROOT, '..', 'stdout.txt')), 'r') as f:
        return filter(lambda e: len(e) > 0, map(lambda e: e.strip(), f.readlines()))

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solutions = map(lambda e: (e[1], __import__(e[0]).deduce_square_root_of), solutions())
        self.inputs = list(map(float, stdin()))
        self.outputs = list(map(float, stdout()))

    def test_solutions(self):
        for id, solution in self.solutions:
            self._assert_solution_expected_output(solution, f'{id}')
            
    def _assert_solution_expected_output(self, solution, id: str):
        assert callable(solution)

        for i, input in enumerate(self.inputs):
            output = solution(input)
            expected = self.outputs[i]
            self.assertEqual(output, expected, f'Expected {expected} but got {output} when calling input {input} on solution {id}.')

if __name__ == '__main__':
    unittest.main()
