import random


def bubble_sort(v):
    comparacoes = trocas = 0
    for fim in range(len(v) - 1, 0, -1):
        mudou = False
        for j in range(fim):
            comparacoes += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocas += 1
                mudou = True
        if not mudou:
            break
    return comparacoes, trocas


def insertion_sort(v):
    comparacoes = movimentos = 0
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if v[j] <= chave:
                break
            v[j + 1] = v[j]
            movimentos += 1
            j -= 1
        v[j + 1] = chave
        movimentos += 1
    return comparacoes, movimentos


def selection_sort(v):
    comparacoes = trocas = 0
    for i in range(len(v) - 1):
        menor = i
        for j in range(i + 1, len(v)):
            comparacoes += 1
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            trocas += 1
    return comparacoes, trocas


def quick_sort(v):
    # Lomuto, pivo final; pilha evita limite de recursao.
    comparacoes = movimentos = 0
    pilha = [(0, len(v) - 1)]
    while pilha:
        inicio, fim = pilha.pop()
        if inicio >= fim:
            continue
        pivo = v[fim]
        i = inicio
        for j in range(inicio, fim):
            comparacoes += 1
            if v[j] <= pivo:
                if i != j:
                    v[i], v[j] = v[j], v[i]
                    movimentos += 2
                i += 1
        if i != fim:
            v[i], v[fim] = v[fim], v[i]
            movimentos += 2
        pilha.append((inicio, i - 1))
        pilha.append((i + 1, fim))
    return comparacoes, movimentos


def executar(original):
    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()
    esperado = sorted(original)  # Apenas validacao externa.
    testes = [
        ("Bubble", bubble_sort, vetor_bubble),
        ("Insertion", insertion_sort, vetor_insertion),
        ("Selection", selection_sort, vetor_selection),
        ("Quick", quick_sort, vetor_quick),
    ]
    resultados = {}
    for nome, algoritmo, vetor in testes:
        comparacoes, contador = algoritmo(vetor)
        assert vetor == esperado, f"Falha: {nome}"
        escritas = 2 * contador if nome in (
            "Bubble", "Selection") else contador
        resultados[nome] = (comparacoes, contador, escritas)
    return resultados


def experimento():
    rng = random.Random(42)
    dados = {}
    for n in (10, 20, 1000):
        original = rng.sample(range(1, 100001), n)
        cenarios = {
            "Aleatorio": original,
            "Ordenado": sorted(original),
            "Inverso": sorted(original, reverse=True),
        }
        dados[n] = {}
        if n <= 20:
            print("Vetor original", n, original)
        for cenario, vetor in cenarios.items():
            resultados = executar(vetor)
            dados[n][cenario] = resultados
            for nome, (comp, contador, escritas) in resultados.items():
                print(n, cenario, nome, comp, contador, escritas,
                      comp + escritas, sep=" | ")
    return dados


if __name__ == "__main__":
    experimento()
