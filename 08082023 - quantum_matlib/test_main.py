import unittest
from test_pauli_operators import TestPauliOperators
# Import other test classes as needed

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestPauliOperators))
    # Add other test classes to the suite

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
