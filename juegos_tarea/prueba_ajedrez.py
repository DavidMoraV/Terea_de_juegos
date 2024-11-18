from ajedrez.Caballo import Caballo
from ajedrez.Alfil import Alfil
from ajedrez.Dama import Dama
from ajedrez.Rey import Rey
from ajedrez.Torre import Torre
from ajedrez.Peon import Peon
from piezas.Coordenada_Ajedrez import CoordenadaAjedrez

def main():
  
    # Alfil: Movimiento válido (diagonal) e inválido (no diagonal)
    un_alfil = Alfil("blanco", CoordenadaAjedrez("b", 2))
    print(un_alfil.mover(CoordenadaAjedrez("d", 4)))  # Debería ser True
    print(un_alfil.mover(CoordenadaAjedrez("e", 4)))  # Debería ser False

    # Peón (negro): Movimiento válido (una casilla hacia atrás) e inválido (demasiadas casillas)
    un_peon_negro = Peon("negro", CoordenadaAjedrez("d", 2))
    print(un_peon_negro.mover(CoordenadaAjedrez("d", 1)))  # Debería ser True
    print(un_peon_negro.mover(CoordenadaAjedrez("d", 4)))  # Debería ser False

    # Peón (blanco): Movimiento válido (una casilla adelante) e inválido (movimiento diagonal no permitido)
    un_peon_blanco = Peon("blanco", CoordenadaAjedrez("d", 4))
    print(un_peon_blanco.mover(CoordenadaAjedrez("d", 5)))  # Debería ser True
    print(un_peon_blanco.mover(CoordenadaAjedrez("e", 6)))  # Debería ser False

    # Torre: Movimiento válido (vertical) e inválido (diagonal)
    una_torre = Torre("blanco", CoordenadaAjedrez("d", 4))
    print(una_torre.mover(CoordenadaAjedrez("d", 8)))  # Debería ser True
    print(una_torre.mover(CoordenadaAjedrez("e", 8)))  # Debería ser False

    # Dama: Movimiento válido (diagonal) e inválido (no en línea recta)
    una_dama = Dama("negro", CoordenadaAjedrez("b", 7))
    print(una_dama.mover(CoordenadaAjedrez("h", 1)))  # Debería ser True
    print(una_dama.mover(CoordenadaAjedrez("e", 8)))  # Debería ser False

    # Caballo: Movimiento válido (en "L") e inválido (no en "L")
    un_caballo = Caballo("negro", CoordenadaAjedrez("a", 1))
    print(un_caballo.mover(CoordenadaAjedrez("b", 3)))  # Debería ser True
    print(un_caballo.mover(CoordenadaAjedrez("b", 2)))  # Debería ser False

    # Rey: Movimiento válido (una casilla en horizontal) e inválido (más de una casilla)
    mi_rey = Rey("negro", CoordenadaAjedrez("e", 3))
    print(mi_rey.mover(CoordenadaAjedrez("f", 3)))  # Debería ser True
    print(mi_rey.mover(CoordenadaAjedrez("b", 2)))  # Debería ser False

# Ejecutar el programa principal
main()
