import tkinter as tk
import math

#Ventana

ventanita= tk.Tk()
ventanita.title("Calculadora")
ventanita.iconbitmap("C:/Users/Luján/Documents/APROYECTOA/CALCU.ico")

ancho_ventana= 468
alto_ventana= 300

ancho_pantalla= ventanita.winfo_screenwidth()
alto_pantalla= ventanita.winfo_screenheight()

pos_x= int((ancho_pantalla / 2) - (ancho_ventana / 2))
pos_y= int((alto_pantalla / 2) - (alto_ventana / 2))

ventanita.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

#Etiquetas

etiquetaTITULO= tk.Label(ventanita , text="CALCULADORA" , font="arial 30", bg= "#FB6C92")

etiquetaVALOR1= tk.Label(ventanita , text="Valor 1(En división dividendo) :" , font="arial 13" , bg="#FFE5EC")
etiquetaVALOR2= tk.Label(ventanita , text="Valor 2(En división divisor) :" , font= "arial 13" , bg="#FFE5EC")

entVALOR1= tk.Entry(ventanita , font="arial 15")
entVALOR2= tk.Entry(ventanita , font="arial 15")


#Funciones y botones

def obtener_valores():
    try:
        valor1 = float(entVALOR1.get())
        valor2 = float(entVALOR2.get())
        return valor1, valor2
    except ValueError:
        resultado.config(text="PON VALORES VALIDOS")
        return None, None

def sumar():
    valor1, valor2 = obtener_valores()
    if valor1 is not None and valor2 is not None:
        resultado.config(text=f"Resultado: {valor1 + valor2}")

def restar():
    valor1, valor2 = obtener_valores()
    if valor1 is not None and valor2 is not None:
        resultado.config(text=f"Resultado: {valor1 - valor2}")

def multiplicar():
    valor1, valor2 = obtener_valores()
    if valor1 is not None and valor2 is not None:
        resultado.config(text=f"Resultado: {valor1 * valor2}")

def dividir():
    valor1, valor2 = obtener_valores()
    if valor1 is not None and valor2 is not None:
        if valor2 != 0:
            resultado.config(text=f"Resultado: {valor1 / valor2}")
        else:
            resultado.config(text="ERROR MATEMÁTICO DA INIFINITO")


botonSUMA= tk.Button(ventanita, text="SUMA", command=sumar,  font="arial 11" , bg="#F55C7A", width=15)
botonRESTA= tk.Button(ventanita, text="RESTA", command=restar, font="arial 11" , bg="#F55C7A", width=15)
botonDIVID= tk.Button(ventanita, text="DIVISIÓN", command=dividir, font="arial 11" , bg="#F55C7A", width=15)
botonMULTI= tk.Button(ventanita, text="MULTIPLICACIÓN", command=multiplicar, font="arial 11", bg="#F55C7A", width=15)

ventanita.configure(bg='#FFE5EC')

#Como se acomoda en la interfaz

ventanita.columnconfigure(0, weight=0)
ventanita.columnconfigure(1, weight=1)

for i in range(7):
    ventanita.rowconfigure(i, weight=1)

etiquetaTITULO.grid(row=0, column=0, columnspan=2, pady=10)

etiquetaVALOR1.grid(row=1 , column=0)
etiquetaVALOR2.grid(row=2 , column=0)

entVALOR1.grid(row=1 , column=1 ,  pady=5)
entVALOR2.grid(row=2 , column=1)

botonSUMA.grid(row=3 , column=0, pady=8 , columnspan= 2 )
botonRESTA.grid(row=4 , column=0 ,pady=8, columnspan= 2 )
botonMULTI.grid(row=5 , column=0 , pady=8, columnspan= 2)
botonDIVID.grid(row=6 , column=0 , pady=8, columnspan= 2)

resultado= tk.Label(ventanita, text="Resultado:", font="arial 15", bg="#FFE5EC")
resultado.grid(row=7, column=0, columnspan=2, pady=10)

ventanita.mainloop()