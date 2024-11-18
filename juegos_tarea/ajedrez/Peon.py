from piezas.piezas import Pieza
from piezas.Coordenada_Ajedrez import CoordenadaAjedrez

class Peon(Pieza):
    def __init__(self, color, coordenada):
        super().__init__(color, coordenada)

    # Método para comparar peones
    def __eq__(self, otro):
        if isinstance(otro, Peon):
            return self.color == otro.color and self.coordenada == otro.coordenada
        return False

    def __str__(self):
        return f"Peón {self.color} en {self.coordenada}"

    # Método para verificar si el movimiento es válido para un peón
    def mover(self, casilla_destino):
        """
        Verifica si el peón puede moverse a la casilla destino.
        Las reglas básicas del movimiento del peón:
        - Los peones blancos solo pueden avanzar hacia adelante (filas más grandes), y los negros hacia atrás (filas más pequeñas).
        - Los peones se mueven un espacio hacia adelante (o dos desde su posición inicial).
        """
        columna_actual = self.coordenada.columna
        fila_actual = self.coordenada.fila

        columna_destino = casilla_destino.columna
        fila_destino = casilla_destino.fila

        # Reglas de movimiento para los peones
        if self.color == "blanco":
            if columna_actual == columna_destino:  # El peón se mueve en la misma columna
                if fila_actual == 2 and fila_destino == 4:  # Puede moverse 2 espacios si está en la fila inicial (2)
                    self.set_coordenada(casilla_destino)
                    return True
                elif fila_destino == fila_actual + 1:  # Puede moverse 1 espacio hacia adelante
                    self.set_coordenada(casilla_destino)
                    return True
        elif self.color == "negro":
            if columna_actual == columna_destino:  # El peón se mueve en la misma columna
                if fila_actual == 7 and fila_destino == 5:  # Puede moverse 2 espacios si está en la fila inicial (7)
                    self.set_coordenada(casilla_destino)
                    return True
                elif fila_destino == fila_actual - 1:  # Puede moverse 1 espacio hacia atrás
                    self.set_coordenada(casilla_destino)
                    return True
        
        # Si no cumple con las reglas de movimiento, es un movimiento inválido
        return False
