import unittest
from validarRFC import validar_rfc  # Asegúrate de importar tu módulo y clase aquí

class TestValidarRFC(unittest.TestCase):

    def test_rfc_valido(self):
        rfc_valido = "ABCD123456XYZ"
        self.assertTrue(validar_rfc(rfc_valido))

    def test_rfc_invalido_longitud(self):
        rfc_invalido = "ABCD12345XYZ"  # Longitud incorrecta
        self.assertFalse(validar_rfc(rfc_invalido))

    def test_rfc_invalido_formato(self):
        rfc_invalido = "1234ABCD5678XYZ"  # Formato incorrecto
        self.assertFalse(validar_rfc(rfc_invalido))

if __name__ == '__main__':
    unittest.main()
