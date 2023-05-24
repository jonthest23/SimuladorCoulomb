from vector import dibujo_vector
from calculos import calculos_cargas

class Carga:
    def __init__(self,valor,ubicacion,canvas) -> None:  # la creacion de la carga implica un valor en coulomb y una ubicacion en el canvas, y canvas
        self.valor = valor
        self.ubicacion = ubicacion
        self.radio = 20
        self.canvas = canvas
        self.tag = None
        self.texto = None
        self.vector = dibujo_vector(self.canvas,self.tag)
        
        
    def dibujar(self,radio = None ,id = None):
        if radio == None:
            radio = self.radio
        x = self.ubicacion[0]
        y = self.ubicacion[1]
        carga_visual = self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill= self.color(), outline="")
        texto = self.canvas.create_text(x, y, text= self.positivoONegativo(), fill="white", font=("Arial", 20)) 
        self.texto = texto
        self.canvas.addtag_withtag(f'carga_{id}', carga_visual) #agregar tag para identificar cargas
        self.canvas.addtag_withtag(f'carga_{id}T', texto) #agregar tag para identificar cargas
        self.tag = f'carga_{id}'
        self.carga_visual = carga_visual
        self.tag_bind()
        
    def positivoONegativo(self):
         if self.valor is not None:
           if self.valor > 0:
               return "+"
           elif self.valor < 0:
                return "-"
           else:
                return "o"
         else:
             return "Error"

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
        radio = self.radio
        self.canvas.coords(self.tag, x - radio, y - radio, x + radio, y + radio)
        self.canvas.coords(f'{self.tag}T', x, y)
    
    def tag_bind(self):
        self.canvas.tag_bind(self.tag, "<ButtonPress-1>", self.empezar_arrastrar)
        self.canvas.tag_bind(self.tag, "<ButtonRelease-1>", self.dejar_arrastrar)
        self.canvas.tag_bind(self.tag + "T", "<ButtonPress-1>", self.empezar_arrastrar)
        self.canvas.tag_bind(self.tag + "T", "<ButtonRelease-1>", self.dejar_arrastrar)

    def update_tag(self,id = None):
        self.tag = f'carga_{id}'
        self.canvas.addtag_withtag(f'carga_{id}', self.carga_visual) #agregar tag para identificar cargas
        self.canvas.addtag_withtag(f'carga_{id}T', self.texto) #agregar tag para identificar cargas
        self.vector.actualizar_tag(self.tag)
   
    def delete_tag(self):
        self.canvas.delete(self.tag)
        self.canvas.delete(f'{self.tag}T')
        self.vector.borrar_vector()
    
    def anadir_vector(self,fin):
        self.vector.definir_vector(fin,self.ubicacion,self.tag,self.canvas)
    
    def borrar_vector(self):
            self.vector.borrar_vector()
    
    def definir_fuerza_vector(self,fin):
        extra = [0,0]
        extra [0] = calculos_cargas().fuerzaaPixels(fin[0]) #fuerza en x
        extra [1] = calculos_cargas().fuerzaaPixels(fin[1]) #fuerza en y
        self.vector.definir_vector(extra,self.ubicacion)

class Cargas_v:
    def __init__(self,canvas) -> None:
        self.canvas = canvas
        self.cargas = []
        self.carga_seleccionada = []
    
    def dibujar(self):
        for carga in self.cargas:
            carga.delete_tag()
        #update tags
        for carga in self.cargas:
            carga.update_tag(self.cargas.index(carga))

        for carga in self.cargas:
            if carga.tag not in self.canvas.find_all():
                carga.dibujar(id = self.cargas.index(carga))

    
    def agregar_carga(self,valor,posicion):
         carga = Carga(valor,posicion,self.canvas)
         #poner logitud del array
         posicion = len(self.cargas)
         carga.dibujar(id = posicion)
         self.cargas.append(carga)
         self.borrarvectores()
    
    def limpiar(self):
        for carga in self.cargas:
            carga.delete_tag()
        self.cargas = []
        dibujo_vector(self.canvas).eliminar_vector_distancia()

    def calcular(self):
        calculos_cargas().calcular_fuerzas(self.cargas)
        

    def eliminar_carga(self,tag):
        tag1= self.arreglar_tags(tag)
        for carga in self.cargas:
            #si tag comienza con carga 
            if f"carga_{self.cargas.index(carga)}" == tag1:
                self.cargas.remove(carga)
                self.canvas.delete(tag1)
                self.canvas.delete(tag1 + "T")
                self.canvas.delete(f'vector_{tag1}')
                break
        self.dibujar()

    def obtener_valor_Tag(self,tag):
        tag1 = self.arreglar_tags(tag)
        for carga in self.cargas:
            if f"carga_{self.cargas.index(carga)}" == tag1:
                return carga.valor
            
    def editar_valor(self,tag,valor):
        tag1= self.arreglar_tags(tag)
        for carga in self.cargas:
            if f"carga_{self.cargas.index(carga)}" == tag1:
                cargaaurreglar = carga
                carga.valor = int(valor)
                break
        cargaaurreglar.delete_tag()
        cargaaurreglar.dibujar(id = self.cargas.index(cargaaurreglar))
    
    def arreglar_tags(self,tag):
        if tag.endswith("T"):
            tag = tag[:-1]
        return tag
        
    def borrarvectores(self,event = None):
        for carga in self.cargas:
            carga.borrar_vector()
        
    
    def seleccionardistancia(self, event):
        if len(self.carga_seleccionada) < 2:
            tags = event.widget.gettags("current")
            for tag in tags:
                if tag.startswith("carga"):
                     if tag.endswith("T"):
                         tag = tag[:-1]
                index = int(tag[6:])
                self.carga_seleccionada.append(self.cargas[index])
                break
                if len(self.carga_seleccionada) == 1:
                    print("Seleccione otra carga")
        if len(self.carga_seleccionada) == 2:
            self.dibujardistancia()
            
    def dibujardistancia(self):
        tag = f"{self.cargas.index(self.carga_seleccionada[0])}_{self.cargas.index(self.carga_seleccionada[1])}"
        dibujo_vector(self.canvas,tag).dibujar_vector_distancia(self.carga_seleccionada[0].ubicacion,self.carga_seleccionada[1].ubicacion)
        


        
        