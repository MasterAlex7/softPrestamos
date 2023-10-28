import unittest
from Amortizacion import AmortizacionDeuda  # Asegúrate de importar correctamente tu clase

class TestAmortizacion(unittest.TestCase):

    def test_calculos_amortizacion(self):
        amortizacion_obj = AmortizacionDeuda(12000, 9, 0.15)  # Renombra la instancia

        objeto = []

        for mes in range(amortizacion_obj.periodo):
            cuota = amortizacion_obj.get_cuota()
            intereses = amortizacion_obj.get_intereses()
            capital = amortizacion_obj.get_capital()
            saldo = amortizacion_obj.get_saldo()

            objeto.append(
                {
                    'Periodo': mes + 1,
                    'Cuota': cuota,
                    'Intereses': intereses,
                    'Capital': capital,
                    'Saldo': saldo
                }
            )

            # Verifica los cálculos
            self.assertAlmostEqual(cuota, objeto[-1]['Cuota'], delta=0.001)
            self.assertAlmostEqual(intereses, objeto[-1]['Intereses'], delta=0.001)
            self.assertAlmostEqual(capital, objeto[-1]['Capital'], delta=0.001)
            self.assertAlmostEqual(saldo, objeto[-1]['Saldo'], delta=0.001)

if __name__ == '__main__':
    unittest.main()
