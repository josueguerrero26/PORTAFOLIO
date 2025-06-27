import customtkinter as ctk

class CalculadoraImpuestos:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title('Calculadora de impuestos')
        self.ventana.geometry('350x250')
        self.ventana.resizable(False,False)

        #Relleno de widgets y tamaño de fuente
        self.padding: dict = {'padx': 20, 'pady': 10}
        self.font = ("Arial", 14) #define el tipo y tamaño defuente
        #realizamos la primera etiqueta ingresos
        self.etiqueta_ingreso = ctk.CTkLabel(self.ventana, text='Ingreso', font=self.font)
        self.etiqueta_ingreso.grid(row=0,column=0, **self.padding)
        #creamos la entrada de texto de ingresos 
        self.entrada_ingreso = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_ingreso.grid(row=0,column=1, **self.padding)
        #creamos la etiqueta de porcentaje 
        self.etiqueta_porcentaje= ctk.CTkLabel(self.ventana, text='Porcentaje:', font=self.font)
        self.etiqueta_porcentaje.grid(row=1, column=0, **self.padding)
        #creamos la entrada de texto de porcentaje 
        self.entrada_porcentaje = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_porcentaje.grid(row=1, column=1, **self.padding)
        #creamos la etiqueta de impuestos 
        self.etiqueta_impuestos = ctk.CTkLabel(self.ventana, text='Impuestos', font=self.font)
        self.etiqueta_impuestos.grid(row=2, column=0, **self.padding)
        #ceamos la entrada de texto de inpuestos 
        self.entrada_resultado = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_resultado.grid(row=2, column=1, **self.padding)
        self.entrada_resultado.insert(0,'0')
        #creamos el boton que realizara la operacion
        self.boton_calcular = ctk.CTkButton(self.ventana, text="Calcular", font=self.font, command=self.calcular_impuesto)
        self.boton_calcular.grid(row=3, column=1, **self.padding)

    def actualizar_resultado(self, texto):
        self.entrada_resultado.insert(0, texto)

    def calcular_impuesto(self):
        self.entrada_resultado.delete(0, ctk.END)
        try:
            ingreso: float = float(self.entrada_ingreso.get())
            porcentaje: float =float(self.entrada_porcentaje.get())
            self.actualizar_resultado(f'${ingreso*(porcentaje/100):,.2f}')
        except ValueError:
            self.actualizar_resultado('Entrada invalida')



    def ejecutar(self):
        """"Ejecutar la aplicacion tkinter."""
        self.ventana.mainloop()




Calculadora = CalculadoraImpuestos()
Calculadora.ejecutar()