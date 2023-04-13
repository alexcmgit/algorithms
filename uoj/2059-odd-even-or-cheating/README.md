<p><a href="https://www.beecrowd.com.br/repository/UOJ_2059_en.html">beecrowd.com.br/repository/UOJ_2059_en.html</a></p><hr>
<div>
  <span>URI Online | 2059</span>
  <h1>Odd, Even or Cheating</h1>
  <div>
    <p>By Marianne Linhares, UFCG <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>A new game called Odd, Even or Cheating is currently (OEC) is now one of the most popular games in the world. This game was created when some friends had no internet connection, no cellphone, no computer, and pretty much nothing to do. The game is so popular that is going to happen the mundial championship of OEC and each country of the world will choose a representant to compete in this championship.</p>
  <p>The game works like this: it's a two players game, the player 1 chooses between odd or even, then each player chooses a positive integer, if the sum of these number is even and player 1 chose even, then player 1 wins, if the sum is odd and player 2 chose odd, then player 2 wins. If player 1 chooses odd he/she wins when the sum is odd, and player 2 wins when the sum is even. Nothing new, right?</p><p>But now there are two more possible moves, player 1 can cheat to make sure that he/she wins independently of the result of the conventional odd or even game, and player 2 can accuse player 1 of cheating. With these additions in the game if player 1 cheats and player 2 accuses him/her of cheating player 2 wins, if player 2 don't accuse and player 1 is cheating then player 1 wins, if player 2 accuses the cheat, but player 1 is not cheating then player 1 wins, if player 1 isn't cheating and player 2 doesn't accuse player 1 then the game will be played as described previously.</p>
  <p>You were hired by OECIO (Odd, Even or Cheating International Organization) to develop a program that given an OEC match it determines the winner.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input consists of one line with 5 integers: <strong>p</strong>, <strong>j1</strong>,<strong> j2</strong>,<strong> r</strong>,<strong> a</strong>. ( 0 ≤ <strong>p, r, a</strong> ≤ 1 e 1 ≤ <strong>j1</strong>, <strong>j2</strong> ≤ 100).</p>
  <p><strong>p</strong> is the player 1 choice (if <strong>p</strong> = 1 then player 1 chooses even, if <strong>p</strong> = 0 then player 1 chooses odd). <strong>j1</strong>, <strong>j2</strong>, represents respectively the numbers that player 1 chose and the number that player 2 chose. <strong>r </strong>represents if player 1 cheated (if <strong>r</strong> = 1 then player 1 cheated, if <strong>r</strong> = 0 then he/she did not), <strong>a</strong> represents if player 2 accused player 1 of cheating (if <strong>a</strong> = 1 then he/she did, if <strong>a</strong> = 0 then he/she did not).</p>
</div>
<h2>Output</h2>
<div>
  <p>Print "Jogador 1 ganha!" if player 1 won or "Jogador 2 ganha!" if player 2 won (no quotation marks).</p>
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
        <p>1 4 5 0 0</p>
      </td>
      <td>
        <p>Jogador 2 ganha!</p>
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
        <p>1 4 5 1 0</p>
      </td>
      <td>
        <p>Jogador 1 ganha!</p>
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
          <p>1 4 5 1 1</p>
        </td>
        <td>
          <p>Jogador 2 ganha!</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Aquecimento para a OBI 2016</p>
</div>