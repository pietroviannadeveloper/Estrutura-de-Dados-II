# Atividade Avaliativa 3
## Análise de algoritmos de ordenação

**Situação-problema:** uma central de distribuição precisa ordenar os códigos de prioridade dos pedidos do menor para o maior.

O experimento compara **Bubble Sort, Insertion Sort, Selection Sort e Quick Sort**, observando a quantidade de operações em vez de medir tempo.

## Arquivos

| Arquivo | Finalidade |
| :--- | :--- |
| [experimento_ordenacao.py](experimento_ordenacao.py) | Implementações, geração dos dados, contadores e validação |
| [relatorio.pdf](relatorio.pdf) | Trabalho completo: metodologia, respostas de a até i, desafio e código |
| [resultados.csv](resultados.csv) | As 36 medições, prontas para análise em uma planilha |

## Como executar

Na raiz do repositório:

```bash
python3 Atividade-Avaliativa-3/experimento_ordenacao.py
```

Ou copie o conteúdo do script para uma célula do Google Colab. Não há dependências externas.

A saída de cada medição segue esta ordem:

```text
tamanho | cenario | algoritmo | comparacoes | contador_original | escritas | total
```

O script imprime os resultados no terminal; o CSV versionado registra a execução usada no relatório.

## Como o experimento foi montado

1. Iniciar `random.Random(42)` uma única vez.
2. Gerar um único vetor para cada tamanho: 10, 20 e 1.000.
3. Sortear números de 1 a 100.000, sem repetição, com `sample`.
4. Criar quatro cópias idênticas, uma por algoritmo.
5. Contar operações durante a ordenação.
6. Comparar a saída com `sorted(original)`, fora da contagem.
7. Repetir com os mesmos valores em ordem crescente e inversa.

A ordem dos tamanhos e o uso do gerador fazem parte da reprodução. Reiniciar a semente dentro do laço altera os vetores.

## Critérios de contagem

| Medida | Critério |
| :--- | :--- |
| Comparações (C) | Apenas relações entre valores; inclui o teste que encerra a busca do Insertion |
| Trocas (T) | Bubble e Selection: uma troca entre posições diferentes conta uma vez |
| Movimentações (M) | Insertion: cada deslocamento e a escrita final da chave; Quick: duas por troca |
| Escritas (E) | Unidade comum: 2 × T no Bubble/Selection; M no Insertion/Quick |
| Total (S) | C + E; indicador didático, não tempo nem contagem de todas as instruções |

Testes de índices, controle de laços, pilha, cópias auxiliares, geração e validação não entram nas contagens. No Insertion, a escrita final conta mesmo quando a chave permanece na posição original. Trocas de uma posição consigo mesma são evitadas.

**Implementações:** Bubble com parada antecipada; Insertion por deslocamentos; Selection sem trocas desnecessárias; Quick com Lomuto, pivô final e pilha explícita. A pilha evita o limite de recursão, mas não elimina o pior caso quadrático.

## Resultados principais

| Tamanho | Bubble C | Bubble T | Insertion C | Insertion M | Selection C | Selection T | Quick C | Quick M |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 45 | 26 | 33 | 35 | 45 | 6 | 29 | 20 |
| 20 | 175 | 87 | 101 | 106 | 190 | 15 | 65 | 54 |
| 1.000 | 498.015 | 243.076 | 244.070 | 244.075 | 499.500 | 994 | 10.234 | 9.756 |

## O que os resultados mostram?

- **Menos comparações nos três vetores aleatórios:** Quick Sort.
- **Menos escritas nos três vetores aleatórios:** Selection Sort.
- **Maior crescimento de C + E entre 10 e 1.000 elementos:** Bubble, de 97 para 984.167.
- **Maior crescimento apenas de comparações:** Selection, de 45 para 499.500.
- **Mesma ordem de complexidade não significa mesma contagem:** os três algoritmos quadráticos fizeram quantidades distintas de operações.

No vetor aleatório de 1.000 elementos, o Quick fez aproximadamente **97,95% menos comparações que o Selection**. Isso não significa a mesma redução no tempo de execução.

## Desafio: a organização inicial muda tudo?

Comparações / escritas, com 1.000 elementos:

| Entrada | Bubble | Insertion | Selection | Quick |
| :--- | ---: | ---: | ---: | ---: |
| Aleatória | 498.015 / 486.152 | 244.070 / 244.075 | 499.500 / 1.988 | 10.234 / 9.756 |
| Crescente | 999 / 0 | 999 / 999 | 499.500 / 0 | 499.500 / 0 |
| Inversa | 499.500 / 999.000 | 499.500 / 500.499 | 499.500 / 1.000 | 499.500 / 1.000 |

**Não afeta todos da mesma maneira.** Bubble otimizado e Insertion aproveitam a ordem crescente. Selection mantém sua busca quadrática. Quick com pivô final cria partições desequilibradas nas entradas crescente e inversa, chegando ao pior caso.

As medições para 10 e 20 elementos também estão no CSV e no relatório.

## Escolha para a central de pedidos

Entre os quatro, o Quick seria minha escolha para lotes geralmente desordenados, com base nas 19.990 operações C + E registradas para 1.000 códigos aleatórios. Para um sistema sujeito a dados ordenados, a estratégia de pivô precisaria ser revista e testada. Escolher um pivô aleatório é uma possível melhoria, **não uma variante medida aqui**.

## Validação e limites

As 36 execuções foram validadas contra a ordenação esperada. As funções também passaram por 880 entradas adicionais, incluindo permutações pequenas, vetores vazios, repetições e sequências ordenadas ou invertidas.

Há uma amostra aleatória por tamanho, conforme o enunciado. O experimento não estima médias de várias amostras, tempo ou memória e não substitui uma demonstração matemática de complexidade.

**Autor:** Pietro Vianna da Rocha · Engenharia de Software

