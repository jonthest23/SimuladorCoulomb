import tkinter as tk
from vector import dibujo_vector
from carga import Cargas_v

class UI:
    def __init__(self):
        self.ventana = None
        self.canvas = None
        self.cargas_v = None
        self.miframe = None
        self.barra_menu = None
        self.mostrar = False
        self.carga_seleccionada = None
        self.mostrar_distancia = None
        


    def crear_ventana(self, titulo, ancho, alto, color="white"):
        ventana = tk.Tk()
        ventana.title(titulo)
        ventana.geometry(f"{ancho}x{alto}")
        self.ventana = ventana
        self.crear_canvas(color)
        self.mostrar_distancia = tk.IntVar()
        self.mostrar_distancia.set(1)
    
    def crear_canvas(self, color):
        canvas = tk.Canvas(self.ventana, bg=color)
        canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas = canvas
    
    def crear_frame_valor(self, texto, color):
        miframe = tk.Frame()
        miframe.config(bg=color)
        label = tk.Label(miframe, text=texto, bg=color,font=("Arial", 12))
        label.pack(padx=6, pady= 2)
        miframe.input = tk.Entry(miframe, borderwidth=2, highlightthickness=2, justify="center")
        miframe.input.pack(padx=6, pady = 4)
        self.miframe = miframe
        
    
    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)
        self.barra_menu = barra_menu
    
    def anadir_opcion(self, label, command):
        self.barra_menu.add_command(label=label, command=command)

    def anadir_checkboton(self, label, variable, command):
        self.barra_menu.add_checkbutton(label=label, variable=variable , command = command)
    
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
    
    def click_derecho_menu(self, event):
        self.ocultar_frame()
        menu = tk.Menu(self.ventana, tearoff=0)
        menu.add_command(label="Agregar carga", command=lambda: self.cargas_v.agregar_carga(0, (event.x, event.y)))
        tags = event.widget.gettags("current")
        for tag in tags:
            if tag.startswith("carga") :
                self.carga_seleccionada = tag
                menu.add_command(label="Modificar valor", command= lambda: self.ocultar_frame(mostrar=True))
                menu.add_command(label="Eliminar", command=lambda: self.cargas_v.eliminar_carga(tag))
                break
        menu.tk_popup(event.x_root, event.y_root)
        
    def draw_grid(self, width, height, cell_size, color):
        for y in range(0, height, cell_size):
            if y % 100 == 0:
                thickness = 2
            else:
                thickness = 1
                
            self.canvas.create_line(0, y, width, y, fill=color , width=thickness)
        for x in range(0, width, cell_size):
            if x % 100 == 0:
                thickness = 2
            else:
                thickness = 1
            self.canvas.create_line(x, 0, x, height, fill=color,width=thickness )

    
    def resize_grid(self, event):
        self.canvas.delete("all")
        self.draw_grid(event.width, event.height, 20, "lightgray")
        self.cargas_v.dibujar()

    def entervalorcarga(self, event):
        valor = self.miframe.input.get()
        self.cargas_v.editar_valor(self.carga_seleccionada,valor)

    def click_izquierdo(self, event):
        self.ocultar_frame(event)
        self.cargas_v.borrarvectores(event)
        if self.mostrar_distancia.get() == 0:
            self.cargas_v.seleccionardistancia(event)
            
    def checkboton(self):
        if self.mostrar_distancia.get() == 1:
            self.barra_menu.entryconfig("Ocultar Distancia", label="Mostrar Distancia")
            
            # Obtener todos los elementos en el lienzo
            elementos = self.canvas.find_all()
            
            # Eliminar los elementos con tags que comienzan con "vectordistancia_"
            dibujo_vector(self.canvas).eliminar_vector_distancia()
        else:
            self.barra_menu.entryconfig("Mostrar Distancia", label="Ocultar Distancia")
            self.cargas_v.carga_seleccionada.clear()


    def run(self):
        self.crear_ventana("Simulador de Coulomb", 990, 440)
        self.cargas_v = Cargas_v(self.canvas)
        self.crear_frame_valor("Ingrese valor en µC", "lightgray")
        self.crear_menu()
        self.anadir_opcion("Calcular", self.cargas_v.calcular)
        self.anadir_opcion("Limpiar", self.cargas_v.limpiar)
        self.anadir_checkboton("Mostrar Distancia", self.mostrar_distancia ,self.checkboton)
        self.canvas.bind("<Configure>", self.resize_grid)
        self.ventana.bind("<Configure>", self.ocultar_frame)
        self.canvas.bind("<Button-3>", self.click_derecho_menu)
        self.canvas.bind("<ButtonPress-1>", self.click_izquierdo)
        self.miframe.input.bind("<Return>", self.entervalorcarga)
        self.draw_grid(990, 440, 20, "lightgray")
        self.ventana.mainloop()



ui = UI()
ui.run()

