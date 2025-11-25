class Tablero:
    def __init__(self, dimensiones, casillas):
        #inicializa los atributos
        self.dimensiones = dimensiones
        self.casillas = casillas

    def mostrar_tablero(self):
        #función usada por __str__ para imprimir resultados
        return "Tablero de dimensiones " + str(self.dimensiones) + " con " + str(self.casillas) + " casillas"

    def __str__(self):
        return self.mostrar_tablero() #llama a mostrar_tablero

if __name__ == "__main__":
    tablero1 = Tablero(3,9) #creo objeto
    print(tablero1) #debería llamar a mostrar_tablero()