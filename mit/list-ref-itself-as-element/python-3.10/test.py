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

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solutions = map(lambda e: (e[1], __import__(e[0]).create_recursive_list), solutions())

    def test_solutions(self):
        for id, solution in self.solutions:
            self._assert_solution_expected_output(solution, f'{id}')
            
    def _assert_solution_expected_output(self, solution, solution_id: str):
        assert callable(solution)

        # No matter how deep, it must always point to the same object id.        
        root = solution()
        child = root[0]
        grandchild = root[0][0][0][0][0][0][0][0][0][0][0][0][0]

        is_same_object = id(root) == id(child) == id(grandchild)

        self.assertTrue(is_same_object, f'Expected a recursive list, but the first element points to different object references on solution {solution_id}.')

if __name__ == '__main__':
    unittest.main()
