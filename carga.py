class Carga:
    def __init__(self,valor,ubicacion,canvas) -> None:  # la creacion de la carga implica un valor en coulomb y una ubicacion en el canvas, y canvas
        self.valor = valor
        self.ubicacion = ubicacion
        radio = 30
        self.canvas = canvas
        self.dibujar(radio)
        
        
    def dibujar(self,radio,):
        x = self.ubicacion[0]
        y = self.ubicacion[1]
        
        carga_visual = self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill= self.color(), outline="")
        self.carga_visual = carga_visual
        self.tag()

    def color(self):
        #color_rgb = (255, 0, 0)  # Color rojo en RGB
        #color_hex = '#%02x%02x%02x' % color_rgb  # Convertir a formato hexadecimal
        if self.valor > 0:
            color = "red"
        elif self.valor < 0:
            color = "blue"
        else:
            color = "grey"
        return color


    def empezar_arrastrar(self,evento):
        self.canvas.bind("<B1-Motion>", self.arrastrar)
    
    def dejar_arrastrar(self,evento):
        self.canvas.unbind("<B1-Motion>")

    def arrastrar(self,evento):
        x = evento.x
        y = evento.y
        self.ubicacion = (x,y)
        radio = 30
        self.canvas.coords(self.carga_visual, x - radio, y - radio, x + radio, y + radio)
    
    def tag(self):
        self.canvas.tag_bind(self.carga_visual, "<ButtonPress-1>", self.empezar_arrastrar)
        self.canvas.tag_bind(self.carga_visual, "<ButtonRelease-1>", self.dejar_arrastrar)
    
        
    

        