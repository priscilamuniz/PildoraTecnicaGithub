import unittest
import os
import ejemplo as ej
import pandas as pd

class TestGastosVerduleria(unittest.TestCase):

    def test_obtener_productos(self):
        
        # Llama a la función y verifica si devuelve los 5 productos esperados
        productos_obtenidos = ej.gastos_verduleria()
        productos_esperados = 5

        self.assertEqual(productos_obtenidos, productos_esperados)

if __name__ == '__main__':
    unittest.main()


