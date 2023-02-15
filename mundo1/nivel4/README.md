# 📝 Atividades
- [x] Problema #1 - [Notas e Moedas](https://www.beecrowd.com.br/judge/pt/problems/view/1021)

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

**Entrada:** O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

**Saída:** Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

<div align="center">

[Solução](./1021.py)

</div>

<hr>

- [x] Problema #2 - [Substituição de Tag](https://www.beecrowd.com.br/judge/pt/problems/view/1254)

Você está no comando de um sistema de documentos que utiliza tags de código numérico para renderizar documentos para impressão. Há um lote de documentos com o texto baseado em tags, que você deve analisar e converter para tags numéricas para a entrada no sistema. Uma tag é iniciada por um caracter '<', que pode ser seguida por letras, números, barras ou espaços, e para finalizar a tag um caracter '>'. As tags não podem ser encaixadas umas nas outras.

As seguintes tags não são válidas:
">HI", "<a<b>c>", "<a b c><", "<a<b>".

As seguintes tags são válidas:
"/=<>HI", "/<>H=I<>/", "<><><><>", "<a=/><b==//bb><c223>", "<a b c>".

Para as comparações entre caracteres deve ser desconsiderado o case sensitive.

**Entrada:** A entrada contém vários casos de teste. Cada caso de teste é composto de três linhas. A primeira linha contém a tag original presente no texto do documento, que irá conter apenas letras (a-z, A-Z), e seu tamanho será entre 1 e 10 caracteres inclusive. A segunda linha contém um valor numérico pela qual a tag original deverá ser substituida, que será um número entre 1 e 1000 inclusive. A terceira e última linha terá entre 1 e 50 caracteres inclusive, e poderá conter os letras (a-z, A-Z), números (0-9), sinal de menor (<), sinal de maior (>), sinais de igual (=), barras (/), ou espaços em branco. Todos os '<' e '>' são usados apenas em tags.

**Saída:** Converto o texto do documento que é dado na entrada, utilizando as específicações dadas acima e imprima em uma única linha, o novo texto do documento com as novas tags, para maiores esclarecimentos consulte o exemplo abaixo.

<div align="center">

[Solução](./1254.py)

</div>

<hr>