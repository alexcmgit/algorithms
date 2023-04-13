<p><a href="https://www.beecrowd.com.br/repository/UOJ_2031_en.html">beecrowd.com.br/repository/UOJ_2031_en.html</a></p><hr>
<div>
  <span>URI Online | 2031</span>
  <h1>Rock, Paper, Airstrike</h1>
  <div>
    <p>By Jeremias Gomes, Universidade de Brasília <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>Rock, Paper, Airstrike is a very popular children’s game, in which two or more children form a circle and do hand gestures in an attempt to get the victory. The rules are surprisingly complex for a children’s game, but it’s still quite popular around the world. </p>
  <p>The games are very simple. Players can choose between the sign of a Rock (fist), the sign of a paper (an open palm), and the signal to the Air Attack (like the paper, but with only the thumb and little finger extended). </p>
  <p><img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_2031.png" style="height:200px; width:200px"></p>
  <p>A game with two players have the following rules to determine a winner:</p>
  <ul>
    <li>Airstrike vs. Rock: In this case, the player with Airstrike defeats the player with Rock for obvious reasons.</li>
    <li>Rock vs. Paper: In this case the player with Rock defeats the one with Paper, because Rock hurts more.</li>
    <li>Paper vs. Airstrike: In here Airstrike wins because Airstrike always wins and Paper is pathetic.</li>
    <li>Paper vs. Paper: In this variation both players win because Paper is useless and no one facing Paper can lose.</li>
    <li>Rock vs. Rock: To this case there is no winner because it depends on what the players decide to do with the Rock and usually do nothing at the end.</li>
    <li>Airstrike vs. Airstrike: When this happens all players lose due to Mutual Annihilation.</li>
  </ul>
  <p>Your task is to write a program that given the choice of two players tell who won the game.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input consist of N (1 ≤ N ≤ 1000) test cases. N should be read in the first line of input. Each test case is composed of two lines each containing a string. The first string is the sign chosen by Player 1 and the second string is the sign chosen by the Player 2. These string can be:</p>
  <ul>
    <li>“ataque”: to represents Airstrike</li>
    <li>“pedra”: to represents Rock</li>
    <li>“papel”: tp represents Paper</li>
  </ul>
</div>
<h2>Output</h2>
<div>
  <p>The output must be contain:</p>
  <ul>
    <li>“Jogador 1 venceu”: if Player 1 has won the game</li>
    <li>“Jogador 2 venceu”: if Player 2 has won the game</li>
    <li>“Ambos venceram”: if the both have won the game</li>
    <li>“Sem ganhador”: if there is no winner</li>
    <li>“Aniquilacao mutua”: if Mutual Annihilation occurs</li>
  </ul>
  <p>Each output of a test case must be in one line.</p>
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
        <p>2<br>
         pedra<br>
         pedra<br>
         ataque<br>
         papel</p>
      </td>
      <td>
        <p>Sem ganhador<br>
         Jogador 1 venceu</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  Warmup of III Maratona de Programação do IFG - Formosa</p>
</div>