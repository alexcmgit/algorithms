<p><a href="https://www.beecrowd.com.br/repository/UOJ_1129_en.html">beecrowd.com.br/repository/UOJ_1129_en.html</a></p><hr>
<div>
  <span>URI Online | 1129</span>
  <h1>Optical Reader</h1>
  <div><p>Maratona de Programação da SBC <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px;"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   Professor John decided to apply only multiple-choice tests to his students. In each test, each question will have five alternatives (A, B, C, D and E), and the teacher will distribute one answer sheet for each student. At the end of the test, the answer sheets will be scanned and processed digitally to obtain the test score for each student. Initially, he asked a nephew, who knows computer programming, to write a program to extract the alternatives marked by the students in the answer sheets. The nephew wrote a good piece of software, but he couldn't finish it because he needs to study for the ICPC contest.</p>
  <br>
  <p>
   During processing, the answer sheets are scanned in gray levels between 0 (full black) and 255 (total white). After detecting the position for the five rectangles corresponding to each of the alternatives of a question, the software calculates the average pixel gray level for each rectangle, returning an integer value corresponding to each alternative. If the rectangle was filled properly the average value is zero (all black). If the rectangle was left blank the average value is 255 (white total). Thus, ideally, if the average values for each alternative of a question are (255, 0, 255, 255, 255), we know that the student has marked alternative <i>B</i> for that question. However, as answer sheets are processed individually, the average gray level for a completely filled rectangle is not necessarily 0 (may be higher), and the value for a rectangle not filled is not necessarily 255 (may be less). Professor John determined that rectangle average gray levels would be divided into two classes: those with values equal or lower to 127 are considered black and those with values higher than 127 will be considered white.<br>
  <br>
   Obviously, not necessarily all questions of all sheets are marked correctly. It can happen that a student makes a mistake and marks more than one alternative for the same question, or does not mark any alternative. In such cases, the answer to the question should be disregarded.<br>
  <br>
   Now, professor John needs a volunteer to write one program that, given the average gray level values of the five rectangles corresponding to the alternatives of a question, determines which alternative was marked, or whether the answer to the question should be disregarded.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input contains several test cases. The first line of a test case contains an integer <strong>N </strong>indicating the number of questions in the answer sheet (1 ≤ <strong>N</strong> ≤ 255).Each of the <strong>N</strong> following lines describes the response to a question and contains five integers <strong>A</strong>, <strong>B</strong>, <strong>C</strong>, <strong>D </strong>and <strong>E</strong>, indicating the values of average gray levels for each alternative (0 ≤ <strong>A</strong>, <strong>B</strong>, <strong>C</strong>, <strong>D</strong>, <strong>E</strong> ≤ 255).<br>
  <br>
   The last test case is followed by a line containing only a number zero.</p>
</div>
<h2>Output</h2>
<div>
  <p>
   For each input test case, your program must print <i>N</i> lines, each line corresponding to a question. If the answer to the question was correctly filled in the answer sheet, the line should contain the alternative selected (‘A’,‘B’, ‘C’, ‘D’ or ‘E’). Otherwise, the line should contain the character ‘*’ (asterisk).</p>
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
           3<br>
           0 255 255 255 255<br>
           255 255 255 255 0<br>
           255 255 127 255 255<br>
           4<br>
           200 200 200 0 200<br>
           200 1 200 200 1<br>
           1 2 3 4 5<br>
           255 5 200 130 205<br>
           0</p>
        </td>
        <td>
          <p>
           A<br>
           E<br>
           C<br>
           D<br>
           *<br>
           *<br>
           B</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   Maratona de Programação da SBC 2010</p>
</div>