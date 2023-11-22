
# me he dado cuenta que no printea el camino mas rapido, simplemente printea uno

def buscar_entrada(mapa):
    for i, row in enumerate(mapa):
        for j, cell in enumerate(row):
            if cell == "A":
                return buscar_salida(mapa, i, j, len(row), len(mapa), 0, [])

    return "NO"

def buscar_salida(mapa, i, j, fil, col, contador, moves):
    if i < 0 or i >= col or j < 0 or j >= fil or mapa[i][j] == '#':
        return False

    if mapa[i][j] == "B":
        print("SÍ")
        print(contador)
        print("".join(moves))
        return True

    mapa[i][j] = '#'

    if buscar_salida(mapa, i + 1, j, fil, col, contador + 1, moves + ["D"]):
        return True
    if buscar_salida(mapa, i - 1, j, fil, col, contador + 1, moves + ["U"]):
        return True
    if buscar_salida(mapa, i, j + 1, fil, col, contador + 1, moves + ["R"]):
        return True
    if buscar_salida(mapa, i, j - 1, fil, col, contador + 1, moves + ["L"]):
        return True

    return False

"""
mapa_ejemplo = [
    list("########"),
    list("#.A#...#"),
    list("#.##.#B#"),
    list("#......#"),
    list("########")
]

"""

n, m = map(int, input().split())
mapa = [list(input().strip()) for _ in range(n)]                # lo prove poniendo mapa = mapa_ejemplo

resultado = buscar_entrada(mapa)

if resultado == "NO":
    print("NO")
