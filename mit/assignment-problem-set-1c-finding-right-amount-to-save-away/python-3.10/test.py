import os
import unittest
import importlib

ROOT = os.path.dirname(os.path.realpath(__file__))

ROOT = os.path.dirname(os.path.realpath(__file__))

def solutions() -> list[str]:
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

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solutions = solutions()
        self.inputs = stdin()
        self.outputs = stdout()

    def test_solutions(self):
        for solution, id in self.solutions:
            self.assert_solution_expected_out(solution, id)

    def assert_solution_expected_out(self, solution, id):
        for i in range(0, len(self.inputs)):
            annual_salary = float(self.inputs[i])
            expected = float(self.outputs[i])

            def exec_solution(solution, *args, **kwargs):
                mod = importlib.import_module(solution)
                return mod.assignment(*args, **kwargs)

            best_savings_rate = exec_solution(solution, annual_salary) or (((), ((''),)),)

            PRECISION = 2

            self.assertAlmostEqual(best_savings_rate, expected, PRECISION, f'Failed for solution {id}: current value of [best_savings_rate]: {best_savings_rate}, expected = {expected}')

            print(F'Solution {id}, Case {i + 1} OK.')


if __name__ == '__main__':
    unittest.main()
