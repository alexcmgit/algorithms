<p><a href="https://www.beecrowd.com.br/repository/UOJ_1076_en.html">beecrowd.com.br/repository/UOJ_1076_en.html</a></p><hr>
<div>
  <span>URI Online | 1076</span>
  <h1>Design Labirints</h1>
  <div><p>
     By Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
  Peter loves to draw mazes, and recently he had an idea: which would be the minimum of pen movements needed to draw a maze, always beginning and finishing at the same position? To make the game more interesting, Peter decided that it is not allowed to lift the pen from the paper. The templates for construction of the maze are always square, 3 x 3, 4 x 4, 5 x 5 up to a maximum of 7 x 7.</p>
  <p>
  For each example, Peter will specify where the drawing must start and your task is to determine the amount of movements required to draw the Peter's maze. Peter remembers that you do not have to worry about cycles, because there will be no cycles in any of the test cases. However, a test case can have an input 4 1 and another input 1 4. This means two lines connecting these same two nodes. Anyway it will make no difference in the drawing of the labyrinth because the amount of movement should be the same.</p>
  <p>
  See the examples below, In the maze(4 x 4), Peter wants to begin in the node 0, draw all lines and return to node 0. For this, the minimum of possible moves is 30. In the maze B (3 x 3), Pedro begins in the node 1, draws all lines and returns to node 1. In this case, he needs 10 movements to make this drawing.<br></p>
  <p><br>
  <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1076.jpg" style="width: 435px; height: 211px;"></p>
</div>
<h2>Entrada</h2>
<div>
  <p>
  The first input line contains an integer <strong>T </strong>(<strong>T </strong>&lt; 100) that represents the number of test cases. Each test case begin with a line containing an integer <strong>N </strong>( <strong>N </strong>&lt; <strong>X<sup>2</sup></strong>, where <strong>X </strong> is the size of the maze that can be from 3 up to 7). This <strong>N </strong> is the node where the drawing must start and also finish. In the next input line there are two informations<strong>V </strong> and <strong>A </strong> that respectively represents the amount of vertices and edges of the maze. Follow <strong>A </strong> lines, each one indicating a line segment that Peter must plot to draw the desired maze.</p>
</div>
<h2>Saída</h2>
<div>
  <p>
   The output should contain one integer for each test case. This number is the amount of movement of pen that must be made to draw the desired maze, considering that the start and end are always from the same point (node) that can not lift the pen from the paper.</p>
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
           2<br>
           0<br>
           16 15<br>
           0 4<br>
           2 3<br>
           6 2<br>
           8 9<br>
           10 9<br>
           8 12<br>
           14 15<br>
           14 10<br>
           6 5<br>
           10 11<br>
           11 7<br>
           4 8<br>
           0 1<br>
           1 2<br>
           12 13<br>
           1<br>
           9 6<br>
           1 2<br>
           1 4<br>
           4 7<br>
           7 8<br>
           4 1<br>
           4 3</p>
        </td>
        <td>
          <p>
           30<br>
           10</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>