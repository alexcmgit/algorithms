<p><a href="https://www.beecrowd.com.br/repository/UOJ_1051_en.html">beecrowd.com.br/repository/UOJ_1051_en.html</a></p><hr>
<div>
  <span>URI Online | 1051</span>
  <h1>Taxes</h1>
  <div>
    <p> By Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif"> Brasil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   In an imaginary country called Lisarb, all the people are very happy to pay their taxes because they know that doesn’t exist corrupt politicians and the taxes are used to benefit the population, without any misappropriation. The currency of this country is Rombus, whose symbol is R$.</p>
  <p>
   Read a value with 2 digits after the decimal point, equivalent to the salary of a Lisarb inhabitant. Then print the due value that this person must pay of taxes, according to the table below.</p>
  <p>
  <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1051_en.png" style="width: 523px; height: 99px;"></p>
  <p>
   Remember, if the salary is R$ 3,002.00 for example, the rate of 8% is only over R$ 1,000.00, because the salary from R$ 0.00 to R$ 2,000.00 is tax free. In the follow example, the total rate is 8% over R$ 1000.00 + 18% over R$ 2.00, resulting in R$ 80.36 at all. The answer must be printed with 2 digits after the decimal point.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input contains only a float-point number, with 2 digits after the decimal point.</p>
</div>
<h2>Output</h2>
<div>
  <p>
   Print the message "R$" followed by a blank space and the total tax to be payed, with two digits after the decimal point. If the value is up to 2000, print the message "Isento". </p>
</div>
<div></div>
  <table>
    <thead>
      <tr>
        <td>Input Samples</td>
        <td>Outputs Samples</td>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>
           3002.00</p>
        </td>
        <td>
          <p>
           R$ 80.36</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           1701.12</p>
        </td>
        <td>
          <p>
           Isento</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           4520.00</p>
        </td>
        <td>
          <p>
           R$ 355.60</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>