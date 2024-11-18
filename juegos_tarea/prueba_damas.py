from damas.Damas import  Ficha
from piezas.piezas import Pieza

def main():
    # Crear una ficha negra en la coordenada (2, 3)(fila, columna)
    ficha_negra = Ficha("negra", (2, 3))
    print(ficha_negra) 

    # Intentar mover la ficha a la coordenada (3, 4)
    try:
        ficha_negra.mover((3, 4))
        print(f"Movimiento a (3, 4) válido: {ficha_negra}")  
    except ValueError as e:                            # "e" es como decir "excepción"
        print(f"Movimiento a (3, 4) inválido: {e}")

    # Intentar mover la ficha a la coordenada (5, 5)
    try:
        ficha_negra.mover((5, 5))
        print(f"Movimiento a (5, 5) válido: {ficha_negra}")
    except ValueError as e:
        print(f"Movimiento a (5, 5) inválido: {e}")

    # Intentar mover la ficha a la coordenada (4, 3)
    try:
        ficha_negra.mover((4, 3))
        print(f"Movimiento a (4, 3) válido: {ficha_negra}")
    except ValueError as e:
        print(f"Movimiento a (4, 3) inválido: {e}")

    # Intentar mover la ficha a la coordenada (5, 4)
    try:
        ficha_negra.mover((5, 4))
        print(f"Movimiento a (5, 4) válido: {ficha_negra}")
    except ValueError as e:
        print(f"Movimiento a (5, 4) inválido: {e}")

if __name__ == "__main__":
    main()