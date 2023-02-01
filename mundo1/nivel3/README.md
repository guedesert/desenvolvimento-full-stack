# 📝 Atividades
- [x] Problema #1 - [Troca de Cartas](https://www.beecrowd.com.br/judge/pt/problems/view/1104)

Alice e Beatriz colecionam cartas de Pokémon. As cartas são produzidas para um jogo que reproduz a batalha introduzida em um dos mais bem sucedidos jogos de videogame da história, mas Alice e Beatriz são muito pequenas para jogar, e estão interessadas apenas nas cartas propriamente ditas. Para facilitar, vamos considerar que cada carta possui um identificador único, que é um número inteiro.

Cada uma das duas meninas possui um conjunto de cartas e, como a maioria das garotas de sua idade, gostam de trocar entre si as cartas que têm. Elas obviamente não têm interesse emtrocar cartas idênticas, que ambas possuem, e não querem receber cartas repetidas na troca.Além disso, as cartas serão trocadas em uma única operação de troca: Alice dá para Beatriz um sub-conjunto com N cartas distintas e recebe de volta um outro sub-conjunto com N cartas distintas.

As meninas querem saber qual é o número máximo de cartas que podem ser trocadas. Por exemplo, se Alice tem o conjunto de cartas {1, 1, 2, 3, 5, 7, 8, 8, 9, 15} e Beatriz o conjunto {2, 2, 2, 3, 4, 6, 10, 11, 11}, elas podem trocar entre si no máximo quatro cartas. Escreva um programa que, dados os conjuntos de cartas que Alice e Beatriz possuem, determine o número máximo de cartas que podem ser trocadas.

**Entrada:** A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois números inteiros A e B, separados por um espaço em branco, indicando respectivamente o número de cartas que Alice e Beatriz possuem (1 ≤ A ≤ 104 e 1 ≤ B ≤ 104). A segunda linha contém A números inteiros Xi, separados entre si por um espaço em branco, cada número indicando uma carta do conjunto de Alice (1 ≤ Xi ≤ 105). A terceira linha contém B números inteiros Yi, separados entre si por um espaço em branco, cada número indicando uma carta do conjunto de Beatriz (1 ≤ Yi ≤ 105). As cartas de Alice e Beatriz são apresentadas em ordem não decrescente.

O final da entrada é indicado por uma linha que contém apenas dois zeros, separados por um espaço em branco.

**Saída:** Para cada caso de teste da entrada seu programa deve imprimir uma única linha, contendo um numero inteiro, indicando o número máximo de cartas que Alice e Beatriz podem trocar entre si.

<p align="center"><a href="./trocadecartas.py">Solução</a></p>

<hr>

- [x] Problema #2 - [Soma de Sobconjuntos](https://www.beecrowd.com.br/judge/pt/problems/view/1690)

Você tem em mãos um array de números inteiros positivos, não necessariamente distintos.

Vamos escolher alguns dos números no array, isto é, um subconjunto não vazio do array original. O valor de um subconjunto é a soma dos elementos contidos nele.

Qual é o menor valor de um subconjunto que não pode ser gerado?


Por exemplo, pegue o array [2, 1, 5]. Os seguintes subconjuntos pode ser formados: [1], [2], [5], [1, 2], [1, 5], [2, 5], [1, 2, 5]. Os seus valores são os seguintes: 1, 2, 5, 3, 6, 7, 8, respectivamente. O valor menor do subconjunto que não pode ser gerado, neste caso, é 4.

**Entrada:** A primeira linha contém um número T (1 ≤ T ≤ 1000), indicando que se seguirão T casos de teste.

Para cada teste, a primeira linha conterá um número N (1 ≤ N ≤ 10000), indicando a quantidade de números que existem no array. A linha seguinte conterá N inteiros positivos separados por espaços, entre 1 a 109.

**Saída:** Para cada caso de teste, imprima uma única linha, a resposta para o problema.

<p align="center"><a href="./somadesubconjuntos.py">Solução</a></p>

<hr>

- [x] Problema #3 - [Conjuntos Bons e Ruins](https://www.beecrowd.com.br/judge/pt/problems/view/2087)

Nesse problema você deverá descobrir se um conjunto de diversas palavras é bom ou ruim. Por definição, um conjunto é bom quando nenhuma palavra desse conjunto é um prefixo de uma outra palavra. Caso contrário, este é considerado um conjunto ruim.

Por exemplo, {abc, dae, abcde} é um conjunto ruim, pois abc é um prefixo de abcde. Quando duas palavras são iguais, definimos como uma sendo prefixo da outra.

**Entrada:** A entrada contém vários casos de teste. A primeira linha de cada caso de teste terá um inteiro N (1 ≤ N ≤ 10⁵), representando a quantidade de palavras no conjunto. Segue então N linhas, cada uma tendo uma palavra de no máximo 100 letras minúsculas. A entrada termina quando N = 0 e não deve ser processada.

**Saída:** Para cada caso de teste, você deverá imprimir Conjunto Bom, ou Conjunto Ruim, conforme explicado acima.

<p align="center"><a href="./conjuntosbonseruins.py">Solução</a></p>

<hr>