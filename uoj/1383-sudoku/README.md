<p><a href="https://www.beecrowd.com.br/repository/UOJ_1383_en.html">beecrowd.com.br/repository/UOJ_1383_en.html</a></p><hr>
<div>
<span>URI Online | 1383</span>
<h1>Sudoku</h1>
<div>Maratona de Programação IME-USP <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt=""> Brazil</div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>The Sudoku puzzle spread quickly across the world, being the most popular hobby in the planet today. Some people, however, fill the matrix incorrectly, breaking the rules. Your task is to write a program that checks whether a filled matrix is a solution to the puzzle or not.</p>
  <p>The matrix is a 9 x 9 matrix of integers. To be considered a solution to the puzzle, each row and each column must contain all integer numbers between 1 and 9. Also, if the matrix is partitioned in nine 3 x 3 sub-matrices (as shown below), each one of them must also contain all numbers between 1 and 9. The following matrix is an example of a solution to the puzzle.</p>
  <p><img alt="" src="https://resources.beecrowd.com.br/gallery/images/novos/Sudoku.png" style="width: 247px; height: 208px; margin-left: 10px; margin-right: 10px;"></p>
</div>
<h2>Input</h2>
<div>
  <p>Several instances are given. The first line of the input contains <strong>n</strong> &gt; 0, the number of matrices in the input. The following lines describe <strong>n</strong> matrices. Each matrix is described by 9 lines. These lines contain 9 integers each.</p>
</div>
<h2>Output</h2>
<div>
  <p>For each instance, your program must print a line containing <em>"Instancia <strong>k</strong></em>" , where <strong>k</strong> is the instance number. In the second line, your program must print "<em>SIM"</em> (portuguese for <em>yes</em>) if the given matrix is a solution to the puzzle, or "<em>NAO</em>" (portuguese for <em>no</em>) otherwise. Print an empty line after each instance.</p>
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
          <p>2<br>
           1 3 2 5 7 9 4 6 8<br>
           4 9 8 2 6 1 3 7 5<br>
           7 5 6 3 8 4 2 1 9<br>
           6 4 3 1 5 8 7 9 2<br>
           5 2 1 7 9 3 8 4 6<br>
           9 8 7 4 2 6 5 3 1<br>
           2 1 4 9 3 5 6 8 7<br>
           3 6 5 8 1 7 9 2 4<br>
           8 7 9 6 4 2 1 5 3<br>
           1 3 2 5 7 9 4 6 8<br>
           4 9 8 2 6 1 3 7 5<br>
           7 5 6 3 8 4 2 1 9<br>
           6 4 3 1 5 8 7 9 2<br>
           5 2 1 7 9 3 8 4 6<br>
           9 8 7 4 2 6 5 3 1<br>
           2 1 4 9 3 5 6 8 7<br>
           3 6 5 8 1 7 9 2 4<br>
           8 7 9 6 4 2 1 3 5</p>
        </td>
        <td>
          <p>Instancia 1<br>
           SIM <br>
          <br>
           Instancia 2<br>
          NAO<br></p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  X Maratona de Programação IME-USP 2006.</p>
</div>