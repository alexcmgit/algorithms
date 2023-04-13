import os
import unittest
from unittest import mock
import importlib

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
        self.solutions = solutions()
        self.inputs = list(map(float, stdin()))
        self.outputs = list(stdout())

    def test_solutions(self):
        for solution, id in self.solutions:
            self.assert_solution_expected_out(solution, id)

    def assert_solution_expected_out(self, solution, id):
        inputs = []
        outputs = []

        for i in range(0, len(self.inputs)):
            inp = self.inputs[i]
            inputs.append(inp)
            outputs.append(self.outputs[i])

            if len(inputs) == 2:
                def exec_test(solution, outputs):
                    mod = importlib.import_module(solution)

                    x, y = inputs

                    square, log = mod.assignment(x, y)
                    exp_square, exp_log = outputs

                    self.assertAlmostEqual(square, float(exp_square))
                    self.assertTrue(f'{log}'.startswith(f'{exp_log}'))

                exec_test(solution, outputs)

                inputs.clear()
                outputs.clear()


if __name__ == '__main__':
    unittest.main()
