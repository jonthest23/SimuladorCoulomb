import tkinter as tk
class dibujo_vector:
    def __init__(self,canvas,tag) -> None:
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

    def definir_vector(self,extra, inicio) :
        fin= (inicio[0] + extra[0],inicio[1] + extra[1])
        posicion_texto = (fin[0] + 10,fin[1] + 10)
        if self.finEIniciodiferentes(fin,inicio) == True:
            vector = self.canvas.create_line(inicio[0],inicio[1],fin[0],fin[1],fill="grey",arrow=tk.LAST, width =4)
            text = self.canvas.create_text(posicion_texto[0],posicion_texto[1],text=f'{self.valor}N',fill="black")
            self.tagtext = f'vector_{self.tagcarga}T'
            self.tag = f'vector_{self.tagcarga}'
            self.canvas.addtag_withtag(self.tag, vector)
            self.canvas.addtag_withtag(self.tagtext, text)
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
            
        

