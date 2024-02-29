import math
import unittest

def calcular_desviacion_estandar(datos):
    n = len(datos)
    if n <= 1:
        return 0
    media = sum(datos) / n
    sumatoria = sum((x - media) ** 2 for x in datos)
    desviacion_estandar = math.sqrt(sumatoria / (n - 1))
    return desviacion_estandar

class TestDesviacionEstandar(unittest.TestCase):
    def test_calculo_desviacion_estandar(self):
        # Caso de prueba con una lista vacía
        self.assertEqual(calcular_desviacion_estandar([]), 0)

        # Caso de prueba con una lista de un solo elemento
        self.assertEqual(calcular_desviacion_estandar([5]), 0)

        # Caso de prueba con una lista de varios elementos
        self.assertAlmostEqual(calcular_desviacion_estandar([1, 2, 3, 4, 5]), 1.5811, places=4)
        self.assertAlmostEqual(calcular_desviacion_estandar([10, 20, 30, 40, 50]), 15.8114, places=4)
        self.assertAlmostEqual(calcular_desviacion_estandar([2, 4, 4, 4, 5, 5, 7, 9]), 2.138, places=4)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
