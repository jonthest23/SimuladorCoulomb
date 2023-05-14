import tkinter as tk
from carga import Carga, Cargas_v

class UI:
    def __init__(self):
        self.ventana = None
        self.canvas = None
        self.cargas_v = None
        self.miframe = None
        self.barra_menu = None


    def crear_ventana(self, titulo, ancho, alto, color="white"):
        ventana = tk.Tk()
        ventana.title(titulo)
        ventana.geometry(f"{ancho}x{alto}")
        self.ventana = ventana
        self.crear_canvas(color)
    
    def crear_canvas(self, color):
        canvas = tk.Canvas(self.ventana, bg=color)
        canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas = canvas
    
    def crear_frame_valor(self, texto, color):
        miframe = tk.Frame()
        miframe.config(bg=color)
        label = tk.Label(miframe, text=texto, bg=color)
        label.pack(padx=10, pady=5)
        input = tk.Entry(miframe)
        input.pack(padx=10, pady=10)
        self.miframe = miframe
    
    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)
        self.barra_menu = barra_menu
    
    def anadir_opcion(self, label, command):
        self.barra_menu.add_command(label=label, command=command)
    
    def mostrar_frame(self, event=None):
        if event is None:
            self.miframe.place(x=10, y=self.ventana.winfo_height() - 90)
        else:
            self.miframe.place(x=event.x, y=event.y)
    
    def click_izquierdo_menu(self, event):
        menu = tk.Menu(self.ventana, tearoff=0)
        menu.add_command(label="Agregar carga", command=lambda: self.cargas_v.agregar_carga(0, (event.x, event.y)))
        tags = event.widget.gettags("current")
        if "carga" in tags:
            menu.add_command(label="Opción adicional", command=self.mostrar_frame)
        menu.tk_popup(event.x_root, event.y_root)
        
    def draw_grid(self, width, height, cell_size, color):
        for y in range(0, height, cell_size):
            self.canvas.create_line(0, y, width, y, fill=color)
        for x in range(0, width, cell_size):
            self.canvas.create_line(x, 0, x, height, fill=color)
    
    def resize_grid(self, event):
        self.canvas.delete("all")
        self.draw_grid(event.width, event.height, 20, "lightgray")
        self.cargas_v.dibujar()

    def run(self):
        self.crear_ventana("Movimiento de Carga", 990, 440)
        self.cargas_v = Cargas_v(self.canvas)
        self.crear_frame_valor("Ingrese valor", "lightgray")
        self.crear_menu()
        self.anadir_opcion("Calcular", self.on_button_click)
        self.anadir_opcion("Limpiar", self.cargas_v.limpiar)
        self.canvas.bind("<Configure>", self.resize_grid)
        self.canvas.bind("<Button-3>", self.click_izquierdo_menu)
        self.draw_grid(990, 440, 20, "lightgray")
        self.ventana.mainloop()

    def on_button_click(self):
        print("calcular")


ui = UI()
ui.run()

