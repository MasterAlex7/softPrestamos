class Amortizacion:
    def __init__(self, dinero, periodo, interes):
        self.dinero = dinero
        self.periodo = periodo
        self.interes = interes
        self.total = dinero * (1 + interes)
    
    def get_capital(self):
        return self.dinero / self.periodo
    
    def get_intereses(self):
        return self.get_capital() * self.interes
    
    def get_saldo(self):
        self.total -= self.get_cuota()
        return self.total
    
    def get_cuota(self):
        return self.get_capital() + self.get_intereses()


Amortizacion = Amortizacion(12000, 9, 0.15)

objeto = []

for mes in range(Amortizacion.periodo):
    objeto.append(
        {
            'Periodo': mes + 1,
            'Cuota': Amortizacion.get_cuota(),
            'Intereses': Amortizacion.get_intereses(),
            'Capital': Amortizacion.get_capital(),
            'Saldo': Amortizacion.get_saldo()
        }
    )

print(objeto)