import tkinter as tk
from carga import Carga, Cargas_v

class UI:
    def __init__(self):
        self.ventana = None
        self.canvas = None
        self.cargas_v = None
        self.miframe = None
        self.barra_menu = None
        self.mostrar = False
        self.carga_seleccionada = None


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
        miframe.input = tk.Entry(miframe)
        miframe.input.pack(padx=10, pady=10)
        self.miframe = miframe
        
    
    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)
        self.barra_menu = barra_menu
    
    def anadir_opcion(self, label, command):
        self.barra_menu.add_command(label=label, command=command)
    
    def ocultar_frame(self, event = None , mostrar = False):
        if mostrar != self.mostrar:

          if event is None:
             if mostrar == True:
               self.mostrar = True
               ubicacion = self.ubicar_frame()
               self.llenarvalorcarga(self.miframe.input)
               self.miframe.place(x = ubicacion[0], y=ubicacion[1])
             else:
              self.mostrar = False
              self.miframe.place_forget()
              
          elif event.widget == self.ventana:
             if mostrar == True:
               self.mostrar = True
               ubicacion = self.ubicar_frame()
               self.miframe.place(x = ubicacion[0], y=ubicacion[1])
             else:
              self.mostrar = False
              self.miframe.place_forget()
          elif event.widget == self.canvas:
               self.mostrar = False
               self.miframe.place_forget()
    

    def llenarvalorcarga(self, input):
        input.delete(0,tk.END)
        input.insert(0,self.cargas_v.obtener_valor_Tag(self.carga_seleccionada))
              
    def ubicar_frame (self, event = None):
        if event == None:
                 ubicacion = [10,self.ventana.winfo_height() - 90]
        elif event.widget == self.ventana:
            ubicacion = [10,event.height - 90]
        return ubicacion
    
    def click_izquierdo_menu(self, event):
        self.ocultar_frame()
        menu = tk.Menu(self.ventana, tearoff=0)
        menu.add_command(label="Agregar carga", command=lambda: self.cargas_v.agregar_carga(0, (event.x, event.y)))
        tags = event.widget.gettags("current")
        for tag in tags:
            if tag.startswith("carga") :
                self.carga_seleccionada = tag
                menu.add_command(label="Modificar valor", command= lambda: self.ocultar_frame(mostrar=True))
                menu.add_command(label="Eliminar", command=lambda: self.cargas_v.eliminar_carga(tag))
                print(tag)
                break
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

    def entervalorcarga(self, event):
        valor = self.miframe.input.get()
        self.cargas_v.editar_valor(self.carga_seleccionada,valor)

    def run(self):
        self.crear_ventana("Movimiento de Carga", 990, 440)
        self.cargas_v = Cargas_v(self.canvas)
        self.crear_frame_valor("Ingrese valor", "lightgray")
        self.crear_menu()
        self.anadir_opcion("Calcular", self.on_button_click)
        self.anadir_opcion("Limpiar", self.cargas_v.limpiar)
        self.canvas.bind("<Configure>", self.resize_grid)
        self.ventana.bind("<Configure>", self.ocultar_frame)
        self.canvas.bind("<Button-1>", self.ocultar_frame)
        self.canvas.bind("<Button-3>", self.click_izquierdo_menu)
        self.miframe.input.bind("<Return>", self.entervalorcarga)
        self.draw_grid(990, 440, 20, "lightgray")
        self.ventana.mainloop()

    def on_button_click(self):
        print("calcular")


ui = UI()
ui.run()

