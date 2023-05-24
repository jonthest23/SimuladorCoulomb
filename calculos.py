from math import sqrt,sin,cos,atan2

class calculos_cargas:
       

    def __init__(self) -> None:
        self.CONSTANTE_COULOMB =  8.9875517873681764*(10**9)
        self.PIXELES_METRO = 200
        self.MULTIPLICADOR_COULOMB = 10**-6 #micro culombios
        self.MULTIPLICADOR_VECTOR = 10**3 #multiplicador para que el vector se vea en la pantalla
        pass

    def calcular_fuerzas(self,cargas):
        for cargaaCalcular in cargas:
            x_fuerza = 0
            y_fuerza = 0
            for cargaEfectora in cargas:
                if self.esDiferenteUbicacion(cargaaCalcular.ubicacion,cargaEfectora.ubicacion) == True:
                    distancia = self.calcular_distancia(cargaaCalcular.ubicacion,cargaEfectora.ubicacion)
                    angulo = self.calcular_angulo(cargaaCalcular.ubicacion,cargaEfectora.ubicacion)
                    fuerza = self.CONSTANTE_COULOMB * ((cargaEfectora.valor * self.MULTIPLICADOR_COULOMB) 
                                                       * (cargaaCalcular.valor * self.MULTIPLICADOR_COULOMB) /(distancia**2))
                    print(fuerza)
                    y_fuerza += (fuerza*sin(angulo))*self.sumarorestar(cargaaCalcular.ubicacion[1],cargaEfectora.ubicacion[1])
                    x_fuerza += (fuerza*cos(angulo))*self.sumarorestar(cargaaCalcular.ubicacion[0],cargaEfectora.ubicacion[0])

            fuerza = round(sqrt(x_fuerza**2 + y_fuerza**2),5)
            cargaaCalcular.vector.valor = fuerza
            cargaaCalcular.definir_fuerza_vector((x_fuerza,y_fuerza))  
        
    def calcular_distancia(self,ubicacion1,ubicacion2):

        x_1 = ubicacion1[0]
        y_1 = ubicacion1[1]
        x = ubicacion2[0]
        y = ubicacion2[1]
        x_diferencia = self.pixelAmetros(x_1 - x)
        y_diferencia = self.pixelAmetros(y_1 - y)
        distancia = sqrt( x_diferencia**2 + y_diferencia** 2)
        return distancia
    
    def calcular_angulo(self,ubicacion1,ubicacion2):
        x_1 = ubicacion1[0]
        y_1 = ubicacion1[1]
        x = ubicacion2[0]
        y = ubicacion2[1]
        x_diferencia = abs(x_1 - x)
        y_diferencia = abs(y_1 - y)
        angulo = atan2(y_diferencia,x_diferencia)
        return angulo
    
    def pixelAmetros(self,pixels):
        return pixels/self.PIXELES_METRO
    
    def metrosApixels(self,metros):
         return round(metros*self.PIXELES_METRO)
    
    def esDiferenteUbicacion (self,ubicacion1,ubicacion2):
        if ubicacion1[0] != ubicacion2[0] and ubicacion1[1] != ubicacion2[1]:
            return True
        else:
            return False
    
    def fuerzaaPixels(self,fuerza):
        return round(fuerza*self.MULTIPLICADOR_VECTOR)
        
    def sumarorestar(self,posicion1,posicion2):
        if posicion1 > posicion2:
            return 1
        elif  posicion1 < posicion2:
            return -1
        


         
            
        
            
    
            

            


            
            


