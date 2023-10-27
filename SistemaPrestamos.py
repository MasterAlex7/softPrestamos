from tkinter import ttk
from tkinter import *
import tkinter as tk
import pymysql.cursors
from tkinter import messagebox
import datetime
import re


class prestamos:
    dbHost = 'localhost'
    dbPort = 3306
    dbUser = 'root'
    dbPassword = 'Alexelpro27'
    dbName = 'sistemaprestamos'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Sistema de Prestamos')
        self.wind.geometry('800x600')

        # Creando un Frame Container
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo usuario')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # RFC de la persona
        Label(frame, text = 'RFC: ').grid(row = 1, column = 0)
        self.rfc = Entry(frame)
        self.rfc.focus()
        self.rfc.grid(row = 1, column = 1)

        # Nombre de la persona
        Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.nombre = Entry(frame)
        self.nombre.grid(row = 2, column = 1)

        # Edad de la persona
        Label(frame, text = 'Edad: ').grid(row = 3, column = 0)
        self.edad = Entry(frame)
        self.edad.grid(row = 3, column = 1)

        # Telefono de la persona
        Label(frame, text = 'Telefono: ').grid(row = 4, column = 0)
        self.telefono = Entry(frame)
        self.telefono.grid(row = 4, column = 1)

        # Correo de la persona
        Label(frame, text = 'Correo: ').grid(row = 5, column = 0)
        self.correo = Entry(frame)
        self.correo.grid(row = 5, column = 1)

        # Boton para agregar un nuevo usuario
        ttk.Button(frame, text = 'Guardar Usuario',command=self.subir_datos).grid(row = 6, columnspan = 2, sticky = W + E)

        frame2 = LabelFrame(self.wind, text = 'Registrar un nuevo prestamo')
        frame2.grid(row = 0, column = 5, columnspan = 3, pady = 20)

        Label(frame2, text = 'RFC: ').grid(row = 1, column = 0)
        self.rfcPrestamo = Entry(frame2)
        self.rfcPrestamo.grid(row = 1, column = 1)

        Label(frame2, text = 'Monto: ').grid(row = 2, column = 0)
        self.monto = Entry(frame2)
        self.monto.grid(row = 2, column = 1)

        Label(frame2, text = 'A cuantos plazos: ').grid(row = 3, column = 0)
        self.plazos = Entry(frame2)
        self.plazos.grid(row = 3, column = 1)

        Label(frame2, text = "Cuanto % de intereses: ").grid(row = 4, column = 0)
        self.intereses = Entry(frame2)
        self.intereses.grid(row = 4, column = 1)

        ttk.Button(frame2, text = 'Generar Prestamo',command=self.subir_prestamo).grid(row = 5, columnspan = 2, sticky = W + E)

    def run_query_add(self,query,parameters = ()):
        MysqlCnx = pymysql.connect(host=self.dbHost,port=self.dbPort,
                                user=self.dbUser,
                                password=self.dbPassword,
                                db=self.dbName,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        cursor = MysqlCnx.cursor()
        cursor.execute(query,parameters)
        MysqlCnx.commit()

    def validar_datos(self):
        if len(self.nombre.get()) != 0 and len(self.telefono.get()) != 0 and len(self.correo.get()) != 0 and len(self.edad.get()) != 0 and len(self.rfc.get()) != 0:
            if self.validar_rfc():
                return True
            else:
                messagebox.showinfo(message="El RFC no es valido", title="Error")
                return False
        else:
            messagebox.showinfo(message="Todos los campos deben estar llenos", title="Error")
            return False

    def validar_rfc(self):
        rfc=self.rfc.get()
        rfc=rfc.upper()
        if len(rfc) == 13:
            if re.match(r'^[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$', rfc):
                return True
            else:
                return False
        else:
            return False

    def subir_datos(self):
        try:
            if self.validar_datos():
                rfc=self.rfc.get()
                rfc=rfc.upper()
                query = "INSERT INTO `cliente` (`rfc`, `nombreCliente`, `edad`, `fecha`, `telefono`, `correo`) VALUES (%s, %s, %s,%s, %s, %s)"
                parameters = (rfc,self.nombre.get(),self.edad.get(),datetime.datetime.now(),self.telefono.get(),self.correo.get())
                self.run_query_add(query,parameters)
                messagebox.showinfo(message="El usuario se ha guardado correctamente", title="Exito")
                self.rfc.delete(0, END)
                self.nombre.delete(0, END)
                self.edad.delete(0, END)
                self.telefono.delete(0, END)
                self.correo.delete(0, END)
        except:
            messagebox.showinfo(message="Ya cuentas con un prestamo", title="Info")

    def validar_datos_prestamo(self):
        return len(self.rfcPrestamo.get()) != 0 and len(self.monto.get()) != 0 and len(self.plazos.get()) != 0 and len(self.intereses.get()) != 0

    def subir_prestamo(self):
        try:
            if self.validar_datos_prestamo():
                query = "INSERT INTO `prestamo` (`rfc`, `monto`, `plazos`, `intereses`) VALUES (%s, %s, %s,%s)"
                parameters = (self.rfcPrestamo.get(),self.monto.get(),self.plazos.get(),self.intereses.get())
                self.run_query_add(query,parameters)
                messagebox.showinfo(message="El prestamo se ha guardado correctamente", title="Exito")
                self.rfcPrestamo.delete(0, END)
                self.monto.delete(0, END)
                self.plazos.delete(0, END)
                self.intereses.delete(0, END)
        except:
            messagebox.showinfo(message="Ha ocurrido un error", title="Error")

if __name__ == '__main__':
    window = Tk()
    application = prestamos(window)
    window.mainloop()