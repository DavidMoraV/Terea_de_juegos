class CoordenadaAjedrez:
    def __init__(self, columna, fila):
        self.columna = columna  # Por ejemplo, 'a', 'b', 'c', etc.
        self.fila = fila        # Por ejemplo, 1, 2, 3, etc.

    def __str__(self):
        return f"{self.columna}{self.fila}"
