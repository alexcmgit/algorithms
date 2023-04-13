<p><a href="https://www.beecrowd.com.br/repository/UOJ_1961_en.html">beecrowd.com.br/repository/UOJ_1961_en.html</a></p><hr>
<div>
  <span>URI Online | 1961</span>
  <h1>Jumping Frog</h1>
  <div>
    <p>By M.C. Pinto, UNILA <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>In each stage of the Jumping Frog game you must safely get your amphibian through a sequence of pipes of different heights to the rightmost pipe. Nevertheless the frog just survives if the height difference of consecutive pipes is at most the frog jump height. If the next pipe height is too high, the frog hits the pipe and fall. If the next pipe height is too low, the frog does not survive the fall. The frog always starts on the top of the leftmost pipe.</p>
  <p>In this game the distance of pipes is irrelevant, which means that the frog always can reach the next pipe with a jump.</p>
  <p align="center"><img alt="" src="https://www.urionlinejudge.com.br/gallery/images/contests/E_1.png" style="height:339px; width:600px"></p>
  <p>You must write a program that, given the pipe heights and the frog jump height, show if the game stage can be beaten or not.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input is given in two lines. The first one has two positive integer numbers <strong>P</strong> and <strong>N</strong>, the frog jump height and the number of pipes (1 ≤ <strong>P</strong> ≤ 5 and 2 ≤ <strong>N</strong> ≤ 100). The second line has <strong>N</strong> positive integer numbers that indicate the pipes heights ordered from left to right. There are no height greater than 10.</p>
</div>
<h2>Output</h2>
<div>
  <p>The output is given in a single line. If the frog can reach the rightmost pipe write "YOU WIN". If the frog fails, write "GAME OVER".</p>
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
        <p>5 10<br>
         1 3 6 9 7 2 4 5 8 3</p>
      </td>
      <td>
        <p>YOU WIN</p>
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
        <p>1 2<br>
         2 2</p>
      </td>
      <td>
        <p>YOU WIN</p>
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
          <p>1 2<br>
           1 3</p>
        </td>
        <td>
          <p>GAME OVER</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Exam 1 of Computer Programming at UNILA (2015, semester 2)</p>
</div>