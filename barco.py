class Barco:
    def __init__(self, nombre, longitud, golpes_recibidos):
        #Inicialización de atributos
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = golpes_recibidos

    def recibir_impacto(self):
        #Aumenta en 1 los golpes recibidos
        self.golpes_recibidos += 1

    def esta_hundido(self):
        #comprueba si está hundido o no
        if self.golpes_recibidos == self.longitud:
            return True
        else:
            return False

    def mostrar_estado(self):
        return str(self.nombre) + " de longitud " + str(self.longitud) + " ha recibido " + str(self.golpes_recibidos) + " golpes"

    def __str__(self):
        self.mostrar_estado()
