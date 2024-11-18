from xianqui.xianqi import General, Consejero, Peon
from piezas.piezas import Pieza

def probar_movimientos():
    # Probar movimientos del General
    general_rojo = General('rojo', 'e1')
    print("\nProbando movimientos del General rojo:")
    try:
        general_rojo.mover('e2')  # Movimiento válido
        print(f"Movimiento válido: General rojo movido a {general_rojo.get_coordenada()}")
    except ValueError as e:
        print(f"Movimiento inválido: {e}")

    try:
        general_rojo.mover('e4')  # Movimiento inválido
        print(f"Movimiento válido: General rojo movido a {general_rojo.get_coordenada()}")
    except ValueError as e:
        print(f"Movimiento inválido: {e}")

    # Probar movimientos del Consejero
    consejero_negro = Consejero('negro', 'e8')
    print("\nProbando movimientos del Consejero negro:")
    try:
        consejero_negro.mover('d9')  # Movimiento válido
        print(f"Movimiento válido: Consejero negro movido a {consejero_negro.get_coordenada()}")
    except ValueError as e:
        print(f"Movimiento inválido: {e}")

    try:
        consejero_negro.mover('e6')  # Movimiento inválido
        print(f"Movimiento válido: Consejero negro movido a {consejero_negro.get_coordenada()}")
    except ValueError as e:
        print(f"Movimiento inválido: {e}")

    # Probar movimientos del Peón
    peon_rojo = Peon('rojo', 'a4')
    print("\nProbando movimientos del Peón rojo:")
    try:
        peon_rojo.mover('a5')  # Movimiento válido antes de cruzar el río
        print(f"Movimiento válido: Peón rojo movido a {peon_rojo.get_coordenada()}")
    except ValueError as e:
        print(f"Movimiento inválido: {e}")

    try:
        peon_rojo.mover('b5')  # Movimiento inválido antes de cruzar el río
        print(f"Movimiento válido: Peón rojo movido a {peon_rojo.get_coordenada()}")
    except ValueError as e:
        print(f"Movimiento inválido: {e}")

if __name__ == "__main__":
    probar_movimientos()

