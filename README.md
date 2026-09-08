<div align="center">

# Estrutura de Dados II
### Do algoritmo à análise: código, experimentos e resultados

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Curso](https://img.shields.io/badge/Engenharia_de_Software-115E59?style=for-the-badge)

**Pietro Vianna da Rocha · Engenharia de Software**

</div>

Este repositório reúne minhas atividades da disciplina de **Estrutura de Dados II**. A proposta é ligar a implementação em Python à análise de complexidade: entender o que o algoritmo faz, contar o trabalho realizado e interpretar o resultado.

## Explore as atividades

| Atividade | Conteúdo disponível | Acesso |
| :--- | :--- | :--- |
| Participação | Relatório em PDF | [Abrir pasta](<Atividade De participação/>) |
| Avaliativa 2 | Notebooks e relatórios, incluindo versões com Bubble e Quick Sort | [Abrir pasta](Atividade-Avaliativa-2/) |
| **Avaliativa 3** | Comparação de quatro algoritmos em uma central de pedidos; código, relatório e dados | [Ver experimento](Atividade-Avaliativa-3/) |

## Em destaque: qual algoritmo ordena melhor os pedidos?

Na [Atividade Avaliativa 3](Atividade-Avaliativa-3/), quatro algoritmos recebem cópias idênticas de vetores com **10, 20 e 1.000 elementos**. O experimento conta comparações e escritas, incluindo entradas aleatórias, crescentes e inversas.

### Resultado para 1.000 elementos aleatórios

| Algoritmo | Comparações | Escritas no vetor |
| :--- | ---: | ---: |
| Bubble Sort | 498.015 | 486.152 |
| Insertion Sort | 244.070 | 244.075 |
| Selection Sort | 499.500 | **1.988** |
| Quick Sort | **10.234** | 9.756 |

> **O contexto muda o resultado.** O Quick fez menos comparações no vetor aleatório, mas chegou a 499.500 nas entradas crescente e inversa. A implementação usa o último elemento como pivô, o que expõe seu pior caso.

Esses números são **contagens de operações, não tempos de execução**. No Bubble e no Selection, uma troca equivale a duas escritas. Os critérios completos estão no [README da atividade](Atividade-Avaliativa-3/README.md).

**[Código Python](Atividade-Avaliativa-3/experimento_ordenacao.py) · [Relatório PDF](Atividade-Avaliativa-3/relatorio.pdf) · [Resultados CSV](Atividade-Avaliativa-3/resultados.csv)**

## Execute o experimento

É necessário apenas **Python 3**. O script usa a biblioteca padrão, sem instalações adicionais.

```bash
git clone https://github.com/pietroviannadeveloper/Estrutura-de-Dados-II.git
cd Estrutura-de-Dados-II
python3 Atividade-Avaliativa-3/experimento_ordenacao.py
```

No Windows, caso o comando disponível seja `python`, utilize-o no lugar de `python3`.

A saída apresenta: tamanho, cenário, algoritmo, comparações, contador original, escritas e soma de comparações com escritas. A semente fixa permite reproduzir os dados mantendo o mesmo código e ambiente de Python.

Para os notebooks da Atividade 2, abra os arquivos `.ipynb` no Google Colab, JupyterLab ou VS Code.

## Conceitos trabalhados

- Arrays, matrizes, índices e percursos.
- Busca sequencial e laços simples ou aninhados.
- Bubble, Insertion, Selection e Quick Sort.
- Contagem de comparações, trocas e movimentações.
- Análise de complexidade e influência da organização inicial.

## Complexidade: um guia de leitura

| Algoritmo / operação | Melhor caso | Caso médio | Pior caso |
| :--- | :---: | :---: | :---: |
| Percurso completo de um array | O(n) | O(n) | O(n) |
| Busca sequencial em matriz | O(1) | O(m × n) | O(m × n) |
| Bubble com parada antecipada | O(n) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

A tabela descreve crescimento assintótico. Ela não determina uma contagem exata nem substitui a análise da implementação e dos dados. O caso médio pressupõe um modelo de entradas; não é uma garantia para qualquer vetor.

## Sobre o repositório

Material acadêmico para acompanhar minha evolução em programação e análise de algoritmos. Os experimentos mantêm código e resultados próximos para facilitar estudo, revisão e reprodução.

**Autor:** [Pietro Vianna da Rocha](https://github.com/pietroviannadeveloper)

**Disciplina:** Estrutura de Dados II

**Curso:** Engenharia de Software

Consulte o arquivo [LICENSE](LICENSE) para os termos de uso.
