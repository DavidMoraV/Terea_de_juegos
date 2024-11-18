from piezas.piezas import Pieza

class Pieza:
    def __init__(self, color, coordenada):
        self.color = color
        self.coordenada = coordenada
    #metodos de color y coordenadas
    def get_color(self):
        return self.color

    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def get_coordenada(self):
        return self.coordenada

    def set_coordenada(self, nueva_coordenada):
        self.coordenada = nueva_coordenada
    
    def es_movimiento_valido(self, nueva_coordenada):
        """Método abstracto. Las piezas específicas implementarán su propia lógica de validación de movimiento."""
        raise NotImplementedError("Este método debe ser implementado por cada pieza específica.")

    def mover(self, nueva_coordenada):
        if self.es_movimiento_valido(nueva_coordenada):
            self.set_coordenada(nueva_coordenada)
        else:
            raise ValueError("Movimiento inválido.")

    def __str__(self):
        return f"Pieza {self.color} en {self.coordenada}"

class Ficha(Pieza):
    def es_movimiento_valido(self, nueva_coordenada):
        fila_actual, columna_actual = self.coordenada
        fila_nueva, columna_nueva = nueva_coordenada

        # Verificar que el movimiento sea diagonal y de una casilla
        return abs(fila_nueva - fila_actual) == 1 and abs(columna_nueva - columna_actual) == 1

    def __str__(self):
        return f"Ficha {self.color} en {self.coordenada}"