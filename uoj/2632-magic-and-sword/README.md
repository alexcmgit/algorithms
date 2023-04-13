<p><a href="https://www.beecrowd.com.br/repository/UOJ_2632_en.html">beecrowd.com.br/repository/UOJ_2632_en.html</a></p><hr>
<div>
  <span>URI Online | 2632</span>
  <h1>Magic and Sword</h1>
  <div>
    <p>By Edson Alves da Costa Júnior, UNB <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>In the Magic and Sword Tower defense, the player can cast area spells to defeat the enemy units. The spells are elemental: fire, water, air and earth, and the affected region is determined by a circle whose radius depends on the level of the spell.</p>
  <p>The table below lists each spell, damage and its radius per level:</p>
  <p><img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_2632.png" style="width:600px; height:160px"></p>
  <p>The enemy units are delimited by a rectangle of width <strong>w</strong> and height <strong>h</strong>, with the lower left corner positioned at the point (x0, y0). The enemy will suffer damage if their bounding rectangle has any intercession with the area defined by the spell circle.</p>
  <p>Given the position and the bounding rectangle of the enemy unit, the center of the explosion, the identifier and level of the spell, determine the damage to the unit. If the unit is out of the spell range, the damage is equal to zero.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input consists of <strong>T</strong> (1 ≤ <strong>T</strong> ≤ 1000) test cases, where the value of <strong>T</strong> is reported in the first line of the input. Each test case consists of two lines. The first contains four integers representing the dimensions <strong>w</strong> and <strong>h</strong> (1 ≤ <strong>w</strong>, <strong>h</strong> ≤ 1000) of the rectangle and the coordinates <strong>x0</strong> and <strong>y0</strong> (0 ≤ <strong>x0</strong>, <strong>y0</strong> ≤ 1000) from the lower left corner. The second line of the test case contains a string with the spell identifier (fire, water, earth and air), the level <strong>N</strong> of this spell (1 ≤ <strong>N</strong> ≤ 3) and the coordinates <strong>cx</strong> e <strong>cy</strong> (0 ≤ <strong>cx</strong>, <strong>cy</strong> ≤ 1000) from the center of the explosion area.</p>
</div>
<h2>Output</h2>
<div>
  <p>For each test case, the output must be the value of the damage received by the unit, followed by a line break.</p>
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
        <p>4</p>
        <p>10 10 50 50</p>
        <p>fire 1 85 55</p>
        <p>10 10 50 50</p>
        <p>fire 2 85 55</p>
        <p>10 10 50 100</p>
        <p>water 3 100 100</p>
        <p>10 10 50 100</p>
        <p>air 3 100 100</p>
      </td>
      <td>
        <p>0</p>
        <p>200</p>
        <p>300</p>
        <p>100</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  Maratona de Programação UnB/CIC 2015.</p>
</div>