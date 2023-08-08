import qutip
import unittest
from uncertainty_relation1 import calculate_inequality

class TestInequality(unittest.TestCase):
    def setUp(self):
        self.sx = qutip.sigmax()
        self.sy = qutip.sigmay()
        self.sz = qutip.sigmaz()

    def test_inequality_sx_sy(self):
        spin_up_x = qutip.basis(2, 0)
        self.assertTrue(calculate_inequality(self.sx, self.sy, spin_up_x))

    def test_inequality_sz_sy(self):
        spin_up_x = qutip.basis(2, 0)
        self.assertTrue(calculate_inequality(self.sz, self.sy, spin_up_x))

if __name__ == "__main__":
    unittest.main()

