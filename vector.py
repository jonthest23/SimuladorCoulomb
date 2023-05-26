import tkinter as tk
from calculos import calculos_cargas
class dibujo_vector:
    def __init__(self,canvas,tag = None) -> None:
        self.tag = None
        self.tagcarga = tag
        self.canvas = canvas
        self.valor = None
        self.tagtext = None
        pass

    def actualizar_tag(self,tag):
        self.tagcarga = tag
        self.tag = f'vector_{self.tagcarga}'
        pass

    def definir_vector(self,extra, inicio , text = None) :
      fin = (inicio[0] + extra[0],inicio[1] + extra[1])
      posicion_texto = (fin[0] + 10,fin[1] + 10)
      if self.finEIniciodiferentes(fin,inicio) == True:
            vector = self.canvas.create_line(inicio[0],inicio[1],fin[0],fin[1],fill="grey",arrow=tk.LAST, width =4)
            text = self.canvas.create_text(posicion_texto[0],posicion_texto[1],text =f'{self.valor}N',fill="black", font = ('Arial', 12))
            self.tagtext = f'vector_{self.tagcarga}T'
            self.tag = f'vector_{self.tagcarga}'
            self.canvas.addtag_withtag(self.tag, vector)
            self.canvas.addtag_withtag(self.tagtext, text)
      pass

    def posicion_texto_dis(self,fin,inicio):
        if inicio[0] > fin[0] and inicio[1] > fin[1]:
                ubicacion_texto = (fin[0] + abs(inicio[0]-fin[0])/2, fin[1] + abs(inicio[1]-fin[1])/2 + 10)
        elif inicio[0] > fin[0] and inicio[1] < fin[1]:
                ubicacion_texto = (fin[0] + abs(inicio[0]-fin[0])/2, fin[1] - abs(inicio[1]-fin[1])/2 - 10)
        elif inicio[0] < fin[0] and inicio[1] > fin[1]:
                ubicacion_texto = (fin[0] - abs(inicio[0]-fin[0])/2, fin[1] + abs(inicio[1]-fin[1])/2 + 10)
        elif inicio[0] < fin[0] and inicio[1] < fin[1]:
                ubicacion_texto = (fin[0] - abs(inicio[0]-fin[0])/2, fin[1] - abs(inicio[1]-fin[1])/2 - 10)
        return ubicacion_texto
        

    def dibujar_vector_distancia(self,fin,inicio):
        if self.finEIniciodiferentes(fin,inicio) == True:
            vector = self.canvas.create_line(inicio[0],inicio[1],fin[0],fin[1],fill="grey",width =3)
            texto = str(calculos_cargas().calcular_distancia(fin,inicio))
            ubicacion_texto = self.posicion_texto_dis(fin,inicio)
            text = self.canvas.create_text(ubicacion_texto[0],ubicacion_texto[1],text =f'{texto} m',fill="black", font = ('Arial', 12))
            self.tagtext = f'vectordistancia_{self.tag}T'
            self.tag = f'vectordistancia_{self.tag}'
            self.canvas.addtag_withtag(self.tag, vector)
            self.canvas.addtag_withtag(self.tagtext, text)
        pass

    def eliminar_vector_distancia(self):
        elementos = self.canvas.find_all()
        for elemento in elementos:
            tags = self.canvas.gettags(elemento)
            for tag in tags:
                if tag.startswith('vectordistancia'):
                    self.canvas.delete(elemento)
        pass



    def borrar_vector(self):
        if self.tag is not None:
            self.canvas.delete(self.tag)
            self.canvas.delete(self.tagtext)
            self.tag = None
            self.valor = None
        pass

    def finEIniciodiferentes(self,fin,inicio):
        if fin[0] != inicio[0] or fin[1] != inicio[1]:
            return True
        else:
            return False
        pass
            
        

