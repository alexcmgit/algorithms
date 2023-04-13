<p><a href="https://www.beecrowd.com.br/repository/UOJ_2486_en.html">beecrowd.com.br/repository/UOJ_2486_en.html</a></p><hr>
        <div>
          <span>URI Online | 2486</span>
          <h1>C Mais ou Menos?</h1>
          <div>
            <p>By João Marcos Salvanini Bellini de Moraes, IFSULDEMINAS <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
          </div>
          <strong>Timelimit: 1</strong>
        </div>
        <div>
        <div>
        <p>Lately, several people are going to Dr. Cláudia Café com Leite to know if they are consuming the recommended daily amount of vitamin C. This exhausted her so she asked you to write a program for her that, given the daily intake of foods rich in vitamin C by a person, returns how much this person has to consume more or less to achieve the recommended amount.</p>
        <p>In order to do such, you can use the following table:</p>
        <table>
        <thead>
          <tr>
            <th>Foods rich in Vitamin C</th>
            <th>Amount of Vitamin C</th>
          </tr>
        </thead>
        <tbody>
        <tr>
          <td>suco de laranja</td>
          <td>120 mg</td>
        </tr>
        <tr>
          <td>morango fresco</td>
          <td>85 mg</td>
        </tr>
        <tr>
          <td>mamao</td>
          <td>85 mg</td>
        </tr>
        <tr>
          <td>goiaba vermelha</td>
          <td>70 mg</td>
        </tr>
        <tr>
          <td>manga</td>
          <td>56 mg</td>
        </tr>
        <tr>
          <td>laranja</td>
          <td>50 mg</td>
        </tr>
        <tr>
          <td>brocolis</td>
          <td>34 mg</td>
        </tr>
      </tbody><tbody>
    </tbody></table>
    <p>Consider the recommended daily intake of vitamin C is between 110 mg and 130 mg, inclusive.</p>
  </div>
  <h2>Input</h2>
  <div>
  <p>Each test case consists of an integer <strong>T</strong> (1 ≤ <strong>T</strong> ≤ 7) indicating that the person daily intakes <strong>T</strong> foods among the 7 foods from the table. The next <strong>T</strong> lines with an integer <strong>N</strong> and a food (lowercase and no blank spaces) indicates that the person intakes an amount <strong>N</strong> of that food. Read input until <strong>T</strong> = 0.</p><p>
</p></div>
<h2>Output</h2>
<div>
  <p>For each test case (<strong>T</strong>), if the intake exceeds the recommended limit, print "<span>Menos X mg</span>", in which X represents how much less the person must consume to reach the recommended limit; if the intake doesn't reach the recommended amount, print "<span>Mais X mg</span>", in which X represents how much more the person must consume to reach the recommended amount; if the intake is between the recommended amount range, print "<span>X mg</span>", in which X represents the daily amount of vitamin C intaken by the person.</p>
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
        <p>2</p>
        <p>2 suco de laranja</p>
        <p>3 mamao</p>
        <p>1</p>
        <p>3 brocolis</p>
        <p>2</p>
        <p>1 manga</p>
        <p>1 laranja</p>
        <p>1</p>
        <p>1 suco de laranja</p>
        <p>0</p>
      </td>
      <td>
        <p>Menos 365 mg</p>
        <p>Mais 8 mg</p>
        <p>Mais 4 mg</p>
        <p>120 mg</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  The Last Contest 2016 - IFSULDEMINAS</p>
</div>