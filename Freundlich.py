import matplotlib.pyplot as plt
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')

# Función para calcular la cantidad adsorbida
def freundlich(K, n, c):
    return K * (c ** (1/n))

# Función para graficar los datos
def plot_data(c_values, q_values):
    plt.plot(c_values, q_values, 'bo-', markersize=8)
    plt.xlabel('Concentración (mg/L)')
    plt.ylabel('Cantidad adsorbida (mg/g)')
    plt.title('Isoterma de adsorción de Freundlich')
    plt.grid(True)
    plt.show()

# Función para procesar los datos ingresados y mostrar la gráfica
def process_data():
    # Obtener los valores de las constantes
    K = float(K_entry.get())
    n = float(n_entry.get())

    # Obtener los valores de concentración ingresados por el usuario
    c_values = [float(c) for c in c_values_entry.get().split()]

    # Calcular la cantidad adsorbida para cada valor de concentración
    q_values = [freundlich(K, n, c) for c in c_values]

    # Graficar los datos
    plot_data(c_values, q_values)

# Crear la ventana principal
root = Tk()
root.title('Cálculo de Adsorción de Freundlich')

# Crear los widgets
K_label = Label(root, text='K:')
K_entry = Entry(root)

n_label = Label(root, text='n:')
n_entry = Entry(root)

c_values_label = Label(root, text='Concentración (mg/L):')
c_values_entry = Entry(root)

calculate_button = Button(root, text='Calcular', command=process_data)

# Ubicar los widgets en la ventana
K_label.grid(row=0, column=0)
K_entry.grid(row=0, column=1)

n_label.grid(row=1, column=0)
n_entry.grid(row=1, column=1)

c_values_label.grid(row=2, column=0)
c_values_entry.grid(row=2, column=1)

calculate_button.grid(row=3, column=0, columnspan=2)

# Ejecutar la ventana
root.mainloop()







        