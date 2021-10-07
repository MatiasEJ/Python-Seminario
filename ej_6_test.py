import unittest
import random
from ej_6 import *

class Test_modulo6(unittest.TestCase):
    def setUp(self) -> None:
        self.lista_fix = [-1,-2,0,1,2,3] 
        self.lista_noFix = [1,4,5]

    def test_estaEnLista(self):
        self.assertEquals(estaEnLista(0,self.lista_fix),True)

    def test_no_estaEnLista(self):
        self.assertEquals(estaEnLista(1,listaRandom(0,10)),True)
    
    def test_inputs(self):
        self.assertEqual(type(estaEnLista(0,self.lista_fix)),bool)

    def test_lista2(self):
        self.assertEquals(estaEnLista2(0,self.lista_fix),True)
        self.assertEquals(estaEnLista2(0,self.lista_fix),True)
        self.assertEquals(estaEnLista2(-14,self.lista_fix),False)
        self.assertNotEquals(estaEnLista2(-15,self.lista_fix),True)
        
    def test_lista3(self):
        self.assertEquals(estaEnLista3(0,self.lista_fix),True)
        self.assertEquals(estaEnLista3(0,[-1,-2,0,1,2]),True)
        self.assertEquals(estaEnLista3(-14,listaRandom(0,10)),False)
        self.assertNotEquals(estaEnLista3(-1,listaRandom(0,10)),True)