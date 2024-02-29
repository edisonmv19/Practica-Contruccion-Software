import unittest


def encontrar_valor_minimo(numeros):
    if len(numeros) == 0:
        return None
    minimo = numeros[0]
    for num in numeros:
        if num < minimo:
            minimo = num
    return minimo


class TestEncontrarValorMinimo(unittest.TestCase):
    def test_valor_minimo(self):
        self.assertEqual(encontrar_valor_minimo([3, 1, 7, 9, 2, 5]), 1)
        self.assertEqual(encontrar_valor_minimo([100, 45, 67, 23, 89]), 23)
        self.assertEqual(encontrar_valor_minimo([5, 5, 5, 5, 5]), 5)
        self.assertEqual(encontrar_valor_minimo([1]), 0)


if __name__ == '__main__':
    unittest.main()
