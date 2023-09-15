import unittest
import qutip
import operators.pauli_operators as pauli_ops

class TestPauliOperators(unittest.TestCase):

    def test_pauli_x(self):
        x_operator = pauli_ops.pauli_x()
        expected_value = qutip.sigmax()
        self.assertEqual(x_operator, expected_value)

    def test_pauli_y(self):
        y_operator = pauli_ops.pauli_y()
        expected_value = qutip.sigmay()
        self.assertEqual(y_operator, expected_value)

    def test_pauli_z(self):
        z_operator = pauli_ops.pauli_z()
        expected_value = qutip.sigmaz()
        self.assertEqual(z_operator, expected_value)

if __name__ == '__main__':
    unittest.main()
