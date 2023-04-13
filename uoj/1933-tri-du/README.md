<p><a href="https://www.beecrowd.com.br/repository/UOJ_1933_en.html">beecrowd.com.br/repository/UOJ_1933_en.html</a></p><hr>
      <div>
        <span>URI Online | 1933</span>
        <h1>Tri-du</h1>
        <div>
          <p>By Ricardo Anido, Universidade Estadual de Campinas <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
        </div>
        <strong>Timelimit: 1</strong>
      </div>
      <div>
      <div>
      <p>Tri-du is a card game inspired in the popular game of Truco. The game uses a normal deck of 52 cards, with 13 cards of each suit, but suits are ignored. What is used is the value of the cards, considered as integers between 1 to 13.</p>
      <p>In the game, each player gets three cards. The rules are simple:</p>
      <p>
    </p><ul>
    <li>A Three of a Kind (three cards of the same value) wins over a Pair (two cards of the same value).</li>
    <li> A Three of a Kind formed by cards of a larger value wins over a Three of a Kind formed by cards of a smaller value.</li>
    <li>A Pair formed by cards of a larger value wins over a Pair formed by cards of a smaller value.</li>
  </ul>
  <p>Note that the game may not have a winner in many situations; in those cases, the cards are returned to the deck, which is re-shuffled and a new game starts.</p>
  <p>A player received already two of the three cards, and knows their values. Your task is to write a program to determine the value of the third card that maximizes the probability of that player winning the game.</p>
</div>
<h2>Input</h2>
<div>
The input consists of a single line, which contains two integers <strong>A</strong> (1 ≤ <strong>A</strong> ≤ 13) and <strong>B</strong> (1 ≤ <strong>B</strong> ≤ 13) that indicates the value of the two first received cards.</div>
<h2>Output</h2>
<div>
  <p>Your program must produce a single line, containing exactly one integer, representing the value of the card that maximizes the probability of the player winning the game.</p>
</div>
<div></div>
<table>
  <thead>
    <tr>
      <td>Input Example</td>
      <td>Output Example</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>10 7</p>
      </td>
      <td>
        <p>10</p>
      </td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>2 2</p>
      </td>
      <td>
        <p>2</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  XX Maratona de Programação da SBC 2015</p>
</div>