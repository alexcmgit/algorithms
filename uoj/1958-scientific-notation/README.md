<p><a href="https://www.beecrowd.com.br/repository/UOJ_1958_en.html">beecrowd.com.br/repository/UOJ_1958_en.html</a></p><hr>
<div>
  <span>URI Online | 1958</span>
  <h1>Scientific Notation</h1>
  <div>
    <p>By M.C. Pinto, UNILA <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>Floating point numbers can be very long to show. In these cases, it is convenient to use the scientific notation.</p>
  <p>You must write a program that, given a floating point number, shows this number in scientific notation: always show the mantissa sign; always show the mantissa with 4 decimal places; use the character 'E' between the mantissa and the exponent; always show the exponent sign; and show the exponent with at least 2 digits.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input is a double precision floating point number <strong>X</strong>&nbsp;(according to the IEEE&nbsp;754-2008 standard). There will never be a number with more than 110 characters&nbsp;long and more than 6 decimal places.</p>
</div>
<h2>Output</h2>
<div>
  <p>The output is the&nbsp;number&nbsp;<strong>X</strong>&nbsp;in a single line&nbsp;using the scientific notation&nbsp;detailed above. See the examples below.</p>
</div>
<div></div>
<table>
  <thead>
    <tr>
      <td>Input Samples</td>
      <td>Output Samples</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>3.141592</p>
      </td>
      <td>
        <p>+3.1416E+00</p>
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
        <p>1.618033</p>
      </td>
      <td>
        <p>+1.6180E+00</p>
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
        <p>602214085774747474747474</p>
      </td>
      <td>
        <p>+6.0221E+23</p>
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
        <p>-0.000027</p>
      </td>
      <td>
        <p>-2.7000E-05</p>
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
          <p>-10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</p>
        </td>
        <td>
          <p>-1.0000E+100</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Exam 1 of Computer Programming at UNILA (2015, semester 2)</p>
</div>