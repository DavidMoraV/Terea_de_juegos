class Pieza:
    def __init__(self, color, coordenada):
        self.color = color
        self.coordenada = coordenada

    def get_color(self):
        return self.color

    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def get_coordenada(self):
        return self.coordenada

    def set_coordenada(self, nueva_coordenada):
        self.coordenada = nueva_coordenada

    def mover(self, nueva_coordenada):
        """Método abstracto. Las piezas específicas implementarán su propia lógica de movimiento."""
        raise NotImplementedError("Este método debe ser implementado por cada pieza específica.")
    
    def __str__(self):
        return f"Pieza {self.color} en {self.coordenada}"