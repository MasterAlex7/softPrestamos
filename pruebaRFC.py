class Amortizacion:
    def __init__(self, dinero, periodo, interes):
        self.dinero = dinero
        self.periodo = periodo
        self.interes = interes
        self.total = dinero * (1 + interes)

   #da el resutado de la columna capital 
    def get_capital(self):
        return self.dinero / self.periodo
    #da el resutado de la columna intereses
    def get_intereses(self):
        return self.get_capital() * self.interes
    #da el resutado de la columna saldo
    def get_saldo(self):
        self.total -= self.get_cuota()
        return self.total
    #da el resutado de la columna cuota
    def get_cuota(self):
        return self.get_capital() + self.get_intereses()

def prueba():
    # Calcula la cuota mensual, interés y capital
    monto = float("1500")
    plazos = int("12")
    intereses = int("10")
    cuota = calcular_cuota(monto, plazos, intereses)
    desglose = calcular_desglose(monto, plazos, intereses, cuota)
                
    # Muestra la tabla con el desglose
    mostrar_desglose(desglose)

def calcular_cuota(monto, plazos, intereses):
    # Realiza los cálculos necesarios para calcular la cuota mensual
    # Puedes usar la fórmula de amortización de préstamos
    cuota = (monto * intereses) / (1 - (1 + intereses) ** -plazos)
    return cuota

def calcular_desglose(monto, plazos, intereses, cuota):
    # Calcula el desglose del préstamo
    desglose = []
    saldo = monto
    for periodo in range(1, plazos + 1):
        interes = saldo * intereses
        capital = cuota - interes
        saldo -= capital
        desglose.append([periodo, cuota, interes, capital, saldo])
        return desglose

def mostrar_desglose(desglose):
    # Crea una tabla o muestra los datos en tu interfaz gráfica
    # Puedes utilizar Tkinter o alguna otra biblioteca gráfica para esto
    # Aquí, se muestra un ejemplo de cómo imprimir los datos en la consola
    for row in desglose:
        print(f"Periodo: {row[0]}, Cuota: {row[1]}, Interés: {row[2]}, Capital: {row[3]}, Saldo: {row[4]}")

prueba()