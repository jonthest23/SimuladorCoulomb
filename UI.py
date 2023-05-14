import tkinter as tk
from carga import Carga
# Función para mover la carga especificar cantidade de pixeles a mover derecha y abajo
# def mover_carga():
#    canvas.move(carga, 5, 0)  # Mueve el círculo 5 píxeles a la derecha y 0 píxeles hacia abajo   (NO NECESIDAD DE MOVIMIENTO)
#    ventana.after(50, mover_carga)  # Llama a la función nuevamente después de 50 milisegundos
def click_izquierdo_menu(event):
    menu = tk.Menu(ventana, tearoff=0)
    menu.add_command(label="Agregar carga", command=lambda: print("Agregar carga"))
    menu.add_command(label="", command=lambda: print("Opción 2 seleccionada"))
    menu.add_separator()
    menu.add_command(label="Salir", command=ventana.quit)
    menu.tk_popup(event.x_root, event.y_root)

def on_button_click():
    print("calcular")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Movimiento de Carga")
ventana.geometry("990x440")

# Crear el lienzo (canvas) donde se mostraran las cargas
canvas = tk.Canvas(ventana, bg="white")
canvas.pack(fill=tk.BOTH, expand=1)

ventana.bind("<Button-3>", click_izquierdo_menu)

# Crear array de cargas
cargas = []

#crear funcion para agregar carga
def agregar_carga():
    carga = Carga(0,(100,100),canvas)
    cargas.append(carga)

# Crear un botón y establecer sus coordenadas
boton = tk.Button(ventana, text="Haz clic aquí", command=on_button_click)
boton.place(x=10, y=10)

agregar_carga()



# Iniciar el movimiento del círculo
#mover

# Ejecutar el bucle principal de la ventana
# import tkinter as tk (NO NECESIDAD DE MOVIMIENTO)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()