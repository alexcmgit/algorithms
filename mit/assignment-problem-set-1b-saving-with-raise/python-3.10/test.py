import os
import unittest
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
        self.inputs = list(stdin())
        self.outputs = list(stdout())

    def test_solutions(self):
        for solution, id in self.solutions:
            self.assert_solution_expected_out(solution, id)


    def assert_solution_expected_out(self, solution, id):
        def parse_percent(percent: str) -> float:
            return float(percent.replace('%', '')) / 100

        for i in range(0, len(self.inputs), 4):
            annual_salary, percent_to_save, dream_home_cost, semi_annual_raise = (float(self.inputs[i]), parse_percent(self.inputs[i + 1]), float(self.inputs[i + 2]), parse_percent(self.inputs[i + 3]))
            expected = float(self.outputs[i // 4])

            def exec_solution(solution, *args, **kwargs):
                mod = importlib.import_module(solution)
                return mod.assignment(*args, **kwargs)

            required_months = exec_solution(solution, annual_salary, percent_to_save, dream_home_cost, semi_annual_raise)

            self.assertTrue(required_months == expected, f'Failed for solution {id}: current value of [required_months]: {required_months}, expected = {expected}')

            print(F'Solution {id}, Case {i // 4 + 1} OK.')


if __name__ == '__main__':
    unittest.main()
