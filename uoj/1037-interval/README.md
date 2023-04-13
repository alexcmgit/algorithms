<p><a href="https://www.beecrowd.com.br/repository/UOJ_1037_en.html">beecrowd.com.br/repository/UOJ_1037_en.html</a></p><hr>
<div>
  <span>URI Online | 1037</span>
  <h1>Interval</h1>
  <div><p>
     Adapted by Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   You must make a program that read a float-point number and print a message saying in which of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read number is less than zero or greather than 100, the program must print the message “Fora de intervalo” that means "Out of Interval".</p>
  <p>
   The symbol '(' represents greather than. For example:<br>
   [0,25] indicates numbers between 0 and 25.0000, including both.<br>
   (25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input file contains a floating-point number.</p>
</div>
<h2>Output</h2>
<div>
  <p>
   The output must be a message like following example.</p>
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
           25.01</p>
        </td>
        <td>
          <p>
           Intervalo (25,50]</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           25.00</p>
        </td>
        <td>
          <p>
           Intervalo [0,25]</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           100.00</p>
        </td>
        <td>
          <p>
           Intervalo (75,100]</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           -25.02</p>
        </td>
        <td>
          <p>
           Fora de intervalo</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>