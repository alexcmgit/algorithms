<p><a href="https://www.beecrowd.com.br/repository/UOJ_1118_en.html">beecrowd.com.br/repository/UOJ_1118_en.html</a></p><hr>
<div>
  <span>URI Online | 1118</span>
  <h1>Several Scores with Validation</h1>
  <div><p>
     By Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>Write an program to read two scores of a student. Calculate and print the semester average. The program must accept only valid scores (a score must fit in the range [0.10]). Each score must be validated separately.</p>
  <p>The program must print a message "novo calculo (1-sim 2-nao)" that means "new calculate (1-yes 2-no)". After, the input will be (1 or 2). 1 means a new calculation, 2 means that the execution must be finished.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input file contains several positive or negative floating-point (double) values​. After the input of 2 valid scores, an integer number <strong>X</strong> will be read. Your program must stop when <strong>X</strong> = 2. </p>
</div>
<h2>Output</h2>
<div>
  <p>If an invalid score is read, must be printed the message "nota invalida". When two valid scores are read, the message "media = " must be printed folowed by the average between these 2 scores. The message "novo calculo (1-sim 2-nao)" must be printed after reading X. This message should be displayed again if the standard input number for X is less than 1 or greater than 2, as example below.</p>
  <p>The output average must be printed with 2 digits after the decimal point.</p>
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
           -3.5<br>
           3.5<br>
           11.0<br>
           10.0<br>
           4<br>
           1<br>
           8.0<br>
           9.0<br>
           2</p>
        </td>
        <td>
          <p>
           nota invalida<br>
           nota invalida<br>
           media = 6.75<br>
           novo calculo (1-sim 2-nao)<br>
           novo calculo (1-sim 2-nao)<br>
           media = 8.50<br>
           novo calculo (1-sim 2-nao)</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   Thanks to Cássio F.</p>
</div>