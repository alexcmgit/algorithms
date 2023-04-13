<p><a href="https://www.beecrowd.com.br/repository/UOJ_1045_en.html">beecrowd.com.br/repository/UOJ_1045_en.html</a></p><hr>
<div>
  <span>URI Online | 1045</span>
  <h1>Triangle Types</h1>
  <div><p>
     Adapted by Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
     Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:<br>
  </p>
  <ul>
    <li>
     if A ≥ B + C, write the message: <strong>NAO FORMA TRIANGULO</strong></li>
    <li>
     if A<sup>2</sup> = B<sup>2</sup> + C<sup>2</sup>, write the message: <strong>TRIANGULO RETANGULO</strong></li>
    <li>
     if A<sup>2</sup> &gt; B<sup>2</sup> + C<sup>2</sup>, write the message: <strong>TRIANGULO OBTUSANGULO</strong></li>
    <li>
     if A<sup>2</sup> &lt; B<sup>2</sup> + C<sup>2</sup>, write the message: <strong>TRIANGULO ACUTANGULO</strong></li>
    <li>
     if the three sides are the same size, write the message: <strong>TRIANGULO EQUILATERO</strong></li>
    <li>
     if only two sides are the same and the third one is different, write the message: <strong>TRIANGULO ISOSCELES</strong></li>
  </ul>
</div>
<h2>Input</h2>
<div>
  <p>
   The input contains three double numbers, A (0 &lt; A) , B (0 &lt; B) and C (0 &lt; C).</p>
</div>
<h2>Output</h2>
<div>
  <p>
   Print all the classifications of the triangle presented in the input.</p>
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
          <p>
           7.0 5.0 7.0</p>
        </td>
        <td>
          <p>
           TRIANGULO ACUTANGULO<br>
           TRIANGULO ISOSCELES</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           6.0 6.0 10.0</p>
        </td>
        <td>
          <p>
           TRIANGULO OBTUSANGULO<br>
           TRIANGULO ISOSCELES</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           6.0 6.0 6.0</p>
        </td>
        <td>
          <p>
           TRIANGULO ACUTANGULO<br>
           TRIANGULO EQUILATERO</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           5.0 7.0 2.0</p>
        </td>
        <td>
          <p>
           NAO FORMA TRIANGULO</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           6.0 8.0 10.0</p>
        </td>
        <td>
          <p>
           TRIANGULO RETANGULO</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>