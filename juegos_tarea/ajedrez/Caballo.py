from piezas.piezas import Pieza
from piezas.Coordenada_Ajedrez import CoordenadaAjedrez

class Caballo(Pieza):
    def __init__(self, color, coordenada):
        super().__init__(color, coordenada)

    # Método para comparar caballos
    def __eq__(self, otro):
        if isinstance(otro, Caballo):
            return self.color == otro.color and self.coordenada == otro.coordenada
        return False

    def __str__(self):
        return f"Caballo {self.color} en {self.coordenada}"

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

    # Método para calcular si el movimiento es válido para un caballo
    def mover(self, casilla_destino):
        """
        Verifica si el caballo puede moverse a la casilla destino.
        Reglas de movimiento del caballo:
        - El caballo se mueve en forma de "L": dos casillas en una dirección y luego una en perpendicular,
          o una casilla en una dirección y luego dos en perpendicular.
        """
        columna_actual = self.coordenada.columna
        fila_actual = self.coordenada.fila

        columna_destino = casilla_destino.columna
        fila_destino = casilla_destino.fila

        # Calcula la diferencia entre la posición actual y la posición de destino
        diferencia_filas = abs(fila_destino - fila_actual)
        diferencia_columnas = abs(ord(columna_destino) - ord(columna_actual))

        # Movimiento en "L": dos casillas en una dirección y una en perpendicular, o viceversa
        if (diferencia_filas == 2 and diferencia_columnas == 1) or (diferencia_filas == 1 and diferencia_columnas == 2):
            self.set_coordenada(casilla_destino)
            return True

        # Movimiento inválido si no cumple con las reglas de movimiento
        return False
