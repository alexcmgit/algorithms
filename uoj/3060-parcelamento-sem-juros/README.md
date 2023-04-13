<p><a href="https://www.beecrowd.com.br/repository/UOJ_3060_en.html">beecrowd.com.br/repository/UOJ_3060_en.html</a></p><hr>
<div>
  <span>URI Online | 3060</span>
  <h1>Parcelamento Sem Juros</h1>
  <div>
    <p>Por <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 01</strong>
</div>
<div>
<div>
  <p>Pedrinho está implementando o sistema de controle de pagamentos parcelados de uma grande empresa de cartão de crédito digital. Os clientes podem parcelar as compras sem juros no cartão, em até <strong>18</strong> vezes. Quando o valor <strong>V</strong> da compra é divisível pelo número P de parcelas que o cliente escolhe, todas as parcelas terão o mesmo valor. Por exemplo, se o cliente comprar um livro de <strong>V = 30</strong> reais em <strong>P = 6</strong> vezes, então as parcelas terão valores: <strong>5, 5, 5, 5, 5</strong> e <strong>5</strong>. Mas se o valor da compra não for divisível pelo número de parcelas será preciso fazer um ajuste, pois a empresa quer que todas as parcelas tenham sempre um valor inteiro e somem no total, claro, o valor exato da compra. O que Pedrinho decidiu foi distribuir o resto da divisão de <strong>V</strong> por <strong>P</strong> igualmente entre as parcelas iniciais. Por exemplo, se a compra for de <strong>V = 45</strong> e o número de parcelas for <strong>P = 7</strong>, então as parcelas terão valores: <strong>7, 7, 7, 6, 6, 6</strong> e <strong>6</strong>. Quer dizer, como o resto da divisão de <strong>45</strong> por <strong>7</strong> é <strong>3</strong>, então as <strong>3</strong> parcelas iniciais devem ter valor um real maior do que as <strong>4</strong> parcelas finais. Você precisa ajudar Pedrinho e escrever um programa que, dado o valor da compra e o número de parcelas, imprima os valores de cada parcela.</p>
</div>
<h2>Entrada</h2>
<div>
  <p>A primeira linha da entrada contém um inteiro <strong>V</strong> , representando o valor da compra. <strong>A</strong> segunda linha da entrada contém um inteiro <strong>P</strong>, indicando o número de parcelas.</p>
</div>
<h2>Saída</h2>
<div>
  <p>Seu programa deve imprimir <strong>P</strong> linhas, cada uma contendo um inteiro representando o valor de uma parcela. A i-ésima linha deve conter o valor da i-ésima parcela, para <strong>1 ≤ i ≤ P</strong>, de acordo com o que Pedrinho decidiu.</p>
  <p><strong>Restrições </strong></p>
  <p><strong>• 10 ≤ V ≤ 1000 </strong></p>
  <p><strong>• 2 ≤ P ≤ 18</strong></p>
</div>
<div></div>
<table>
  <thead>
    <tr>
      <td>Exemplos de Entrada</td>
      <td>Exemplos de Saída</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>30</p>
        <p>6</p>
      </td>
      <td>
        <p>5</p>
        <p>5</p>
        <p>5</p>
        <p>5</p>
        <p>5</p>
        <p>5</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <table>
    <thead>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>45</p>
          <p>7</p>
        </td>
        <td>
          <p>7</p>
          <p>7</p>
          <p>7</p>
          <p>6</p>
          <p>6</p>
          <p>6</p>
          <p>6</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Olimpíada Brasileira de Informática – OBI2019 – Prog. Nível Júnior – Fase Nacional</p>
</div>