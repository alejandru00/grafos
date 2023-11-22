def contar_habitaciones(n, m, mapa):
    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or mapa[i][j] == '#':
            return
        mapa[i][j] = '#'                                        # las visitadas
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(i + di, j + dj)

    num_habitaciones = 0
    for i in range(n):
        for j in range(m):
            if mapa[i][j] == '.':
                num_habitaciones += 1
                dfs(i, j)

    return num_habitaciones

"""
mapa_ejemplo = [
    list("########"),
    list("#..#...#"),
    list("####.#.#"),
    list("#..#...#"),
    list("########")
]

"""

n, m = map(int, input().split())
mapa = [list(input().strip()) for _ in range(n)]                # lo prove poniendo mapa = mapa_ejemplo        

resultado = contar_habitaciones(n, m, mapa)
print(resultado)                                                # mas bonico

