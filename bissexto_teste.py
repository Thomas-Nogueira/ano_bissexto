import unittest
from bissexto import is_bissexto

class TesteBissexto(unittest.TestCase):

    def teste_ano_eh_inteiro(self):
        try:
            is_bissexto(1)
            pass
        except:
            self.fail("Isso nao deveria ter acontecido")

    def teste_ano_nao_eh_inteiro(self):
        with self.assertRaises(TypeError):
            is_bissexto("hu3hu3uh3")

    def teste_ano_maior_que_zero(self):
        self.assertFalse(is_bissexto(1))

    def teste_ano_menor_ou_igual_zero(self):
        with self.assertRaises(ValueError):
            is_bissexto(0)

    def teste_ano_divisivel_por_4_e_nao_100(self):
        self.assertTrue(is_bissexto(4))
    
    def teste_ano_divisivel_100_e_400(self):
        self.assertTrue(is_bissexto(400))

    def teste_ano_nao_divisivel_4(self):
        self.assertFalse(is_bissexto(5))
        self.assertFalse(is_bissexto(7))

    def teste_ano_nao_divisivel_400(self):
        self.assertFalse(is_bissexto(500))
    
    def teste_dojo_puzzle(self):
        """
        São bissextos por exemplo:

            1600
            1732
            1888
            1944
            2008

        Não são bissextos por exemplo:

            1742
            1889
            1951
            2011
        """
        self.assertTrue(is_bissexto(1600))
        self.assertTrue(is_bissexto(1732))
        self.assertTrue(is_bissexto(1888))
        self.assertTrue(is_bissexto(1944))
        self.assertTrue(is_bissexto(2008))

        self.assertFalse(is_bissexto(1742))
        self.assertFalse(is_bissexto(1889))
        self.assertFalse(is_bissexto(1951))
        self.assertFalse(is_bissexto(2011))
    
if __name__ == '__main__':
    unittest.main()