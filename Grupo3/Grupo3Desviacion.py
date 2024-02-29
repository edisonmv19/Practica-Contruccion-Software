import math
import unittest

def calcular_desviacion_estandar(numeros):
    if len(numeros) < 2:
        raise ValueError("Se requieren al menos dos números para calcular la desviación estándar")
    
    # Calcular la media
    media = sum(numeros) / len(numeros)
    
    # Calcular la suma de los cuadrados de las diferencias
    sum_cuadrados_diff = sum((x - media) ** 2 for x in numeros)
    
    # Calcular la desviación estándar
    desviacion_estandar = math.sqrt(sum_cuadrados_diff / len(numeros))
    
    return desviacion_estandar

class TestCalcularDesviacionEstandar(unittest.TestCase):
    def test_desviacion_estandar(self):
        # Prueba con un conjunto de números conocidos
        numeros = [1, 2, 3, 4, 5]
        resultado = calcular_desviacion_estandar(numeros)
        self.assertAlmostEqual(resultado, 1.5811, places=4)
        print("La función pasó con éxito.")

    def test_desviacion_estandar_con_un_elemento(self):
        # Prueba con un solo elemento
        numeros = [5]
        with self.assertRaises(ValueError):
            calcular_desviacion_estandar(numeros)

    def test_desviacion_estandar_con_ningun_elemento(self):
        # Prueba con una lista vacía
        numeros = []
        with self.assertRaises(ValueError):
            calcular_desviacion_estandar(numeros)

    def test_desviacion_estandar_con_dos_elementos(self):
        # Prueba con dos elementos
        numeros = [5, 5]
        resultado = calcular_desviacion_estandar(numeros)
        self.assertAlmostEqual(resultado, 0, places=4)
        print("La función paso con exito.")

if _name_ == '_main_':
    unittest.main()