<p><a href="https://www.beecrowd.com.br/repository/UOJ_1309_en.html">beecrowd.com.br/repository/UOJ_1309_en.html</a></p><hr>
<div>
  <span>URI Online | 1309</span>
  <h1>Monetary Formatting</h1>
  <div><p> Por TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif"> EUA</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   Often it is necessary to write monetary amounts in a standard format. We decided formatting quantities in the following way:<br>
   &nbsp;&nbsp;&nbsp;1. The montande must begin with '$';<br>
   &nbsp;&nbsp;&nbsp;2. The number must end with a decimal point and exactly two digits following;<br>
   &nbsp;&nbsp;&nbsp;3. The digits to the left of the decimal point must separate in groups of three oir commas.</p>
  <p>
   Your task in this problem is to create a program that, given two integer values ​​to dollars and cents return String formatted properly.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input consists of several test cases. Each test case consists of two integers, <strong>dollars</strong> (0 ≤ <strong>dollars</strong>&nbsp;≤ 2 * 10<sup>9</sup>) and <strong>cents</strong> (0 ≤ <strong>cents</strong> ≤ 99), respectively.</p>
</div>
<h2>Output</h2>
<div>
  <p>For each test case print a string formatted according to the formatting rules.</p>
</div>
<div></div>
  <table>
    <thead>
      <tr>
        <td>Sample Input</td>
        <td>Sample Output</td>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>
           123456<br>
           0<br>
           49734321<br>
           9<br>
           20502030<br>
           70</p>
        </td>
        <td>
          <p>
           $123,456.00<br>
           $49,734,321.09<br>
           $20,502,030.70</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   * Este problema é de autoria do TopCoder (www.topcoder.com/tc) e foi adaptado por Mateus Lazarotto para utilização (autorizada) no URI OJ.<br>
   * A reprodução não autorizada deste problema sem o consentimento por escrito de TopCoder, Inc. é estritamente proibida.</p>
</div>