<p><a href="https://www.beecrowd.com.br/repository/UOJ_2702_en.html">beecrowd.com.br/repository/UOJ_2702_en.html</a></p><hr>
<div>
  <span>URI Online | 2702</span>
  <h1>Hard Choice</h1>
  <div>
    <p>By Inés Kereki, ACM ICPC 2017 <img src="https://resources.beecrowd.com.br/gallery/images/flags/uy.gif" alt="UY"> Uruguay</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>In long flights, airlines offer hot meals. Usually the flight attendants push carts containing the meals down along the aisles of the plane. When a cart reaches your row, you are asked right away: “Chicken, beef, or pasta?” You know your choices, but you have only a few seconds to choose and you don’t know how your choice will look like because your neighbor hasn’t opened his wrap yet. . .</p>
  <p>The flight attendant in this flight decided to change the procedure. First she will ask all passengers what choice of meal they would prefer, and then she will check if the number of meals available in this flight for each choice are enough.</p>
  <p>As an example, consider that the available number of meals for chicken, beef and pasta are respectively (80, 20, 40), while the number of passenger’s choices for chicken, beef and pasta are respectively (45, 23, 48). In this case, eleven people will surely not receive their selection for a meal, since three passengers who wanted beef and eight passengers who wanted pasta cannot be pleased.</p>
  <p>Given the quantity of meals available for each choice and the number of meals requested for each choice, could you please help the flight attendant to determine how many passengers will surely not receive their selection for a meal?</p>
</div>
<h2>Input</h2>
<div>
  <p>The first line contains three integers <strong>C<sub>a</sub></strong>, <strong>B<sub>a</sub></strong> and <strong>P<sub>a</sub></strong> (0 ≤ <strong>C<sub>a</sub></strong>, <strong>B<sub>a</sub></strong>, <strong>P<sub>a</sub></strong> ≤ 100), representing respectively the number of meals available for chicken, beef and pasta. The second line contains three integers <strong>C<sub>r</sub>,</strong> <strong>B<sub>r</sub></strong> and <strong>P<sub>r</sub></strong> (0 ≤ <strong>C<sub>r</sub></strong>, <strong>B<sub>r</sub></strong>, <strong>P<sub>r</sub></strong> ≤ 100), indicating respectively the number of meals requested for chicken, beef and pasta.</p>
</div>
<h2>Output</h2>
<div>
  <p>Output a single line with an integer representing the number of passengers that will surely not receive their selection for a meal.</p>
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
        <p>80 20 40</p>
        <p>45 23 48</p>
      </td>
      <td>
        <p>11</p>
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
        <p>0 0 0</p>
        <p>100 100 100</p>
      </td>
      <td>
        <p>300</p>
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
          <p>41 42 43</p>
          <p>41 42 43</p>
        </td>
        <td>
          <p>0</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  ACM/ICPC Latin American Regional 2017</p>
</div>