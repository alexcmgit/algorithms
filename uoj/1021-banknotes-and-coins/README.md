<p><a href="https://www.beecrowd.com.br/repository/UOJ_1021_en.html">beecrowd.com.br/repository/UOJ_1021_en.html</a></p><hr>
<div>
  <span>URI Online | 1021</span>
  <h1>Banknotes and Coins</h1>
  <div><p>
     By Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of <em> notes</em> and <em>coins </em>on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input file contains a value of floating point <strong>N </strong>(0 ≤ <strong>N </strong>≤ 1000000.00).</p>
</div>
<h2>Output</h2>
<div>
  <p>
   Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.</p>
</div>
<div></div>
  <table>
    <thead>
      <tr>
        <td>Input Sample</td>
        <td>Output Sample</td>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>
           576.73</p>
        </td>
        <td>
          <p>
           NOTAS:<br>
           5 nota(s) de R$ 100.00<br>
           1 nota(s) de R$ 50.00<br>
           1 nota(s) de R$ 20.00<br>
           0 nota(s) de R$ 10.00<br>
           1 nota(s) de R$ 5.00<br>
           0 nota(s) de R$ 2.00<br>
           MOEDAS:<br>
           1 moeda(s) de R$ 1.00<br>
           1 moeda(s) de R$ 0.50<br>
           0 moeda(s) de R$ 0.25<br>
           2 moeda(s) de R$ 0.10<br>
           0 moeda(s) de R$ 0.05<br>
           3 moeda(s) de R$ 0.01</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           4.00</p>
        </td>
        <td>
          <p>
           NOTAS:<br>
           0 nota(s) de R$ 100.00<br>
           0 nota(s) de R$ 50.00<br>
           0 nota(s) de R$ 20.00<br>
           0 nota(s) de R$ 10.00<br>
           0 nota(s) de R$ 5.00<br>
           2 nota(s) de R$ 2.00<br>
           MOEDAS:<br>
           0 moeda(s) de R$ 1.00<br>
           0 moeda(s) de R$ 0.50<br>
           0 moeda(s) de R$ 0.25<br>
           0 moeda(s) de R$ 0.10<br>
           0 moeda(s) de R$ 0.05<br>
           0 moeda(s) de R$ 0.01</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           91.01</p>
        </td>
        <td>
          <p>
           NOTAS:<br>
           0 nota(s) de R$ 100.00<br>
           1 nota(s) de R$ 50.00<br>
           2 nota(s) de R$ 20.00<br>
           0 nota(s) de R$ 10.00<br>
           0 nota(s) de R$ 5.00<br>
           0 nota(s) de R$ 2.00<br>
           MOEDAS:<br>
           1 moeda(s) de R$ 1.00<br>
           0 moeda(s) de R$ 0.50<br>
           0 moeda(s) de R$ 0.25<br>
           0 moeda(s) de R$ 0.10<br>
           0 moeda(s) de R$ 0.05<br>
           1 moeda(s) de R$ 0.01</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>