<p><a href="https://www.beecrowd.com.br/repository/UOJ_1040_en.html">beecrowd.com.br/repository/UOJ_1040_en.html</a></p><hr>
<div>
  <span>URI Online | 1040</span>
  <h1>Average 3</h1>
  <div><p>
     Adapted by Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   Read four numbers (N<sub>1</sub>, N<sub>2</sub>, N<sub>3</sub>, N<sub>4</sub>), which one with 1 digit after the decimal point, corresponding to 4 scores obtained by a student. Calculate the average with weights 2, 3, 4 e 1 respectively, for these 4 scores and print the message <em>"Media: " </em>(Average), followed by the calculated result. If the average was 7.0 or more, print the message <em>"Aluno aprovado."</em> (Approved Student). If the average was less than 5.0, print the message: <em>"Aluno reprovado."</em> (Reproved Student). If the average was between 5.0 and 6.9, including these, the program must print the message "Aluno em exame." (In exam student).</p>
  <p>
  In case of exam, read one more score. Print the message <em>"Nota do exame: "</em> (Exam score) followed by the typed score. Recalculate the average (sum the exam score with the previous calculated average and divide by 2) and print the message <em>“Aluno aprovado.”</em> (Approved student) in case of average 5.0 or more) or <em>"Aluno reprovado."</em> (Reproved student) in case of average 4.9 or less. For these 2 cases (approved or reproved after the exam) print the message <em>"Media final: "</em> (Final average) followed by the final average for this student in the last line.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input contains four floating point numbers that represent the students' grades.</p>
</div>
<h2>Output</h2>
<div>
  <p>
   Print all the answers with one digit after the decimal point.</p>
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
           2.0 4.0 7.5 8.0<br>
           6.4</p>
        </td>
        <td>
          <p>
           Media: 5.4<br>
           Aluno em exame.<br>
           Nota do exame: 6.4<br>
           Aluno aprovado.<br>
           Media final: 5.9</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           2.0 6.5 4.0 9.0</p>
        </td>
        <td>
          <p>Media: 4.8<br>
           Aluno reprovado.</p>
        </td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr>
        <td>
          <p>
           9.0 4.0 8.5 9.0</p>
        </td>
        <td>
          <p>
           Media: 7.3<br>
           Aluno aprovado.</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>