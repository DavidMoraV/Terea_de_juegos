from piezas.piezas import Pieza
from piezas.Coordenada_Ajedrez import CoordenadaAjedrez

class Alfil(Pieza):
    def __init__(self, color, coordenada):
        super().__init__(color, coordenada)

    # Método para comparar alfiles
    def __eq__(self, otro):
        if isinstance(otro, Alfil):
            return self.color == otro.color and self.coordenada == otro.coordenada
        return False

    def __str__(self):
        return f"Alfil {self.color} en {self.coordenada}"

    # Métodos para el color
    def get_color(self):
        return self.color

    def set_color(self, nuevo_color):
        self.color = nuevo_color

    # Método para obtener la posición actual
    def get_coordenada(self):
        return self.coordenada

    # Método para actualizar la posición
    def set_coordenada(self, nueva_coordenada):
        self.coordenada = nueva_coordenada

    # Método para calcular si el movimiento es válido para un alfil
    def mover(self, casilla_destino):
        """
        Verifica si el alfil puede moverse a la casilla destino.
        El alfil se mueve en diagonal, cualquier número de casillas.
        """
        # Accede a los atributos `columna` y `fila` de `CoordenadaAjedrez`
        columna_actual = self.coordenada.columna
        fila_actual = self.coordenada.fila

        columna_destino = casilla_destino.columna
        fila_destino = casilla_destino.fila

        # Calcula las diferencias en filas y columnas
        diferencia_filas = abs(fila_destino - fila_actual)
        diferencia_columnas = abs(ord(columna_destino) - ord(columna_actual))

        # El alfil se mueve en diagonal, por lo que las diferencias deben ser iguales
        if diferencia_filas == diferencia_columnas:
            self.set_coordenada(casilla_destino)
            return True

        # Movimiento inválido si no cumple con las reglas de movimiento
        return False
