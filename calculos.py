from math import sqrt,sin,cos , atan2, pi

class calculos_cargas:
       

    def __init__(self) -> None:
        self.CONSTANTE_COULOMB =  8.9875517873681764*(10**9)
        self.PIXELES_METRO = 200
        self.MULTIPLICADOR_COULOMB = 10**-6 #micro culombios
        self.MULTIPLICADOR_VECTOR = 10**3 #multiplicador para que el vector se vea en la pantalla
        pass

    def calcular_fuerzas(self,cargas):
        x_fuerza = 0
        y_fuerza = 0
        for carga in cargas:
            x_fuerza = 0
            y_fuerza = 0
            for carga2 in cargas:
                if self.esDiferenteUbicacion(carga.ubicacion,carga2.ubicacion) == True:
                    distancia = self.calcular_distancia(carga.ubicacion,carga2.ubicacion)
                    angulo = self.calcular_angulo(carga.ubicacion,carga2.ubicacion)
                    fuerza = self.CONSTANTE_COULOMB * (abs(carga2.valor * self.MULTIPLICADOR_COULOMB )
                          *abs(carga.valor * self.MULTIPLICADOR_COULOMB))/(distancia**2)
                    y_fuerza += (fuerza*sin(angulo))*self.sumarorestar(carga.valor,carga2.valor,carga.ubicacion[1],carga2.ubicacion[1])
                    x_fuerza += (fuerza*cos(angulo))*self.sumarorestar(carga.valor,carga2.valor,carga.ubicacion[0],carga2.ubicacion[0])
                x_fuerza += 0
                y_fuerza += 0
            x_fuerzas = self.fuerzaaPixels(x_fuerza)
            y_fuerzas = self.fuerzaaPixels(y_fuerza)
            fuerza = round(sqrt(x_fuerzas**2 + y_fuerzas**2),2)
            carga.vector.valor = fuerza
            carga.vector.definir_vector((x_fuerzas,y_fuerzas),carga.ubicacion)
            
            
        
    def calcular_distancia(self,ubicacion1,ubicacion2):

        x_1 = ubicacion1[0]
        y_1 = ubicacion1[1]
        x = ubicacion2[0]
        y = ubicacion2[1]
        x_diferencia = self.pixelAmetros(abs(x_1 - x))
        y_diferencia = self.pixelAmetros(abs(y_1 - y))
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
        print(round(fuerza*self.MULTIPLICADOR_VECTOR))
        return round(fuerza*self.MULTIPLICADOR_VECTOR)
        
    
    def esNegativalaDiferencia(self,valor1,valor2):
        if valor1 > valor2:
            return True
        else:
            return False
    def sonMismoSigno(self,valor1,valor2):
        if valor1 > 0 and valor2 > 0:
            return True
        elif valor1 < 0 and valor2 < 0:
            return True
        else:
            return False
        
    def sumarorestar(self,valor1,valor2,posicion1,posicion2):
        if self.sonMismoSigno(valor1,valor2) == True and posicion1 > posicion2:
            return 1
        elif self.sonMismoSigno(valor1,valor2) == True and posicion1 < posicion2:
            return -1
        elif self.sonMismoSigno(valor1,valor2) == False and posicion1 > posicion2:
            return -1
        elif self.sonMismoSigno(valor1,valor2) == False and posicion1 < posicion2:
            return 1


         
            
        
            
    
            

            


            
            


