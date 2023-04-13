<p><a href="https://www.beecrowd.com.br/repository/UOJ_1436_en.html">beecrowd.com.br/repository/UOJ_1436_en.html</a></p><hr>
<div>
<span>URI Online | 1436</span>
<h1>Brick Game</h1>
<div>By Arifuzzaman Arif <img src="https://resources.beecrowd.com.br/gallery/images/flags/bd.gif" alt=""> Bangladesh</div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   There is a village in Bangladesh, where brick game is very popular. Brick game is a team game. Each team consists of odd number of players. Number of players must be greater than 1 but cannot be greater than 10. Age of each player must be within 11 and 20. No two players can have the same age. There is a captain for each team. The communication gap between two players depends on their age difference, i.e. the communication gap is larger if the age difference is larger. Hence they select the captain of a team in such a way so that the number of players in the team who are younger than that captain is equal to the number of players who are older than that captain.</p>
  <p>
   Ages of all members of the team are provided. You have to determine the age of the captain.</p>
</div>
<h2>Input</h2>
<div>
  <p>Input starts with an integer <strong>T (T ≤ 100)</strong>, the number of test cases. Each of the next <strong>T</strong> lines will start with an integer <strong>N (1 &lt; N &lt; 11)</strong>, number of team members followed by <strong>N</strong> space separated integers representing ages of all of the members of a team. Each of these N integers will be between <strong>11</strong> and <strong>20</strong> (inclusive). Note that, ages will be given in strictly increasing order or strictly decreasing order. We will not mention which one is increasing and which one is decreasing, you have to be careful enough to handle both situations.</p>
</div>
<h2>Output</h2>
<div>
  <p>For each test case, output one line in the format <strong>“Case x: a”</strong> (quotes for clarity), where <strong>x</strong> is the case number and a is the age of the captain.</p>
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
           5 19 17 16 14 12<br>
           5 12 14 16 17 18</p>
        </td>
        <td>
          <p>Case 1: 16<br>
           Case 2: 16</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Adapted by Gerson Groth.</p>
</div>