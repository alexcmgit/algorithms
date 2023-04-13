<p><a href="https://www.beecrowd.com.br/repository/UOJ_1087_en.html">beecrowd.com.br/repository/UOJ_1087_en.html</a></p><hr>
    <div>
    <span>URI Online | 1087</span>
    <h1>Queen</h1>
    <div><p>
       By Fábio Dias Moreira&nbsp;<img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px;">&nbsp;Brazil</p></div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
       The game of Chess has several pieces with curious movements. One of them is the <i>Queen</i>, which can move any number of squares in any direction: in the same line, in the same column or in any of the diagonals, as illustrated by the figure below (black dots represent positions the queen may reach in one move):</p>
      <p>
      <br> <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1087.png" style="width: 147px; height: 145px;"></p> <br>
      <p>
       The great Chess Master Kary Gasparov invented a new type of chess problem: given the position of a queen in an empty standard chess board (that is, an 8 x 8 board) how many moves are needed so that she reaches another given square in the board?</p>
      <p>
       Kary found the solution for some of those problems, but is having a difficult time to solve some others, and therefore he has asked that you write a program to solve this type of problem.</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>
       The input contains several test cases. The only line of each test case contains four integers <i>X<sub>1</sub></i>, <i>Y<sub>1</sub></i>, <i>X<sub>2</sub></i> and <i>Y<sub>2</sub></i> (<i>1 ≤ X<sub>1</sub>, Y<sub>1</sub>, X<sub>2</sub>, Y<sub>2</sub> ≤ 8</i>). The queen starts in the square with coordinates <i>(X<sub>1</sub>, Y<sub>1</sub>)</i>, and must finish at the square with coordinates <i>(X<sub>2</sub>, Y<sub>2</sub>)</i>. In the chessboard, columns are numbered from 1 to 8, from left ro right; lines are also numbered from 1 to 8, from top to bottom. The coordinates of a square in line <i>X</i> and column <i>Y</i> are (<i>X, Y</i>).</p>
      <p>
       The end of input is indicated by a line containing four zeros, separated by spaces.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
       For each test case in the input your program must print a single line, containing an integer, indicating the smallest number of moves needed for the queen to reach the new position.</p>
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
           4 4 6 2<br>
           3 5 3 5<br>
           5 5 4 3<br>
           0 0 0 0</p>
        </td>
        <td>
          <p>
           1<br>
           0<br>
           2</p>
        </td>
      </tr>
    </tbody>
  </table> <p>
   Maratona de Programação da SBC 2008.</p>
</div>