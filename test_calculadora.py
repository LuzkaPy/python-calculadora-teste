# test_calculadora.py
import unittest
from calculadora import adicao, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):

    def test_adicao(self):
        self.assertEqual(adicao(2, 3), 5)
        self.assertEqual(adicao(-2, 3), 1)
        self.assertEqual(adicao(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(-2, 3), -5)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 3), 6)
        self.assertEqual(multiplicacao(-2, 3), -6)
        self.assertEqual(multiplicacao(0, 0), 0)

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2)
        self.assertEqual(divisao(-6, 3), -2)
        self.assertEqual(divisao(0, 1), 0)

        # Teste de divisão por zero deve levantar ValueError
        with self.assertRaises(ValueError):
            divisao(1, 0)

if __name__ == "__main__":
    unittest.main()
