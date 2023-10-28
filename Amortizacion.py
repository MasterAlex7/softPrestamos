class AmortizacionDeuda:
    def __init__(self, dinero, periodo, interes):
        self.dinero = dinero
        self.periodo = periodo
        self.interes = interes
        self.total = dinero * (1 + interes)
    
    def get_capital(self):
        return round(self.dinero / self.periodo, 3)
    
    def get_intereses(self):
        return round(self.get_capital() * self.interes,3)
    
    def get_saldo(self):
        self.total -= self.get_cuota()
        return round(self.total,3)
    
    def get_cuota(self):
        return round(self.get_capital() + self.get_intereses(),3)


Amortizacion = AmortizacionDeuda(12000, 9, 0.15)

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