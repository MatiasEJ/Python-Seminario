import unittest
import random
from ej_61 import *

class Test_modulo6(unittest.TestCase):
    def setUp(self) -> None:
        self.lista_fix = [-1,-2,0,1,2,3] 
        self.lista_noFix = [1,4,5]

    def test_estaEnLista(self):
        self.assertEqual(estaEnLista(0,self.lista_fix),True)
        self.assertEqual(estaEnLista(0,[]),False)

    
    def test_inputs(self):
        self.assertEqual(type(estaEnLista(0,self.lista_fix)),bool)

    def test_lista2(self):
        self.assertEqual(estaEnLista2(0,self.lista_fix),True)
        self.assertEqual(estaEnLista2(0,[]),False)

        self.assertEqual(estaEnLista2(0,self.lista_fix),True)
        self.assertEqual(estaEnLista2(-14,self.lista_fix),False)
        self.assertNotEqual(estaEnLista2(-15,self.lista_fix),True)
        
    def test_lista3(self):
        self.assertEqual(estaEnLista3(0,self.lista_fix),True)
        self.assertEqual(estaEnLista3(0,[]),False)
        self.assertEqual(estaEnLista3(0,[-1,-2,0,1,2]),True)
        self.assertEqual(estaEnLista3(-14,listaRandom(0,10)),False)
        self.assertNotEqual(estaEnLista3(-1,listaRandom(0,10)),True)

if __name__ == '__main__':
    unittest.main()