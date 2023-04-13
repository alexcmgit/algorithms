<p><a href="https://www.beecrowd.com.br/repository/UOJ_1160_en.html">beecrowd.com.br/repository/UOJ_1160_en.html</a></p><hr>
<div>
  <span>URI Online | 1160</span>
  <h1>Population Increase</h1>
  <div><p>
     Adapted by Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   Mariazinha wants to solve an interesting problem. Given the population and growing rate of 2 cities (A and B), she would like to know how many years would be necessary to the smaller city (always A) to be greater than the larger city (always B) in population. Of course, she only wants to know the result for cities that the growing rate for city A is bigger than the growing rate for city B, therefore, she separated these test cases for you. Your job is to build a program that print the time in years for each test case.</p>
  <p>
   However, in some cases the time can be so big and Mariazinha don't want to know the exact time for these cases. In this way, for these test cases, it is enough printing the message "Mais de 1 seculo", that means "More than a Century".</p>
</div>
<h2>Input</h2>
<div>
<p>
The first line of the input contains a single integer <strong>T</strong>, indicating the number of test cases (1 ≤ <strong>T</strong> ≤ 3000). Each test case contains four numbers: two integers <strong>PA</strong> and <strong>PB</strong> (100 ≤ <strong>PA</strong> &lt; 1000000, 100 ≤ <strong>PB</strong> ≤ 1000000, <strong>PA</strong> &lt; <strong>PB</strong>) indicating respectively the population of A and B and two numbers <strong>G1</strong> and <strong>G2</strong>
 (0.1 ≤ <strong>G1</strong> ≤ 10.0, 0.0 ≤ <strong>G2</strong> ≤ 10.0, <strong>G2</strong> &lt; <strong>G1</strong>) with one digit after the decimal point each, indicating the populational growing (in percentual) for A and B respectively. </p>
<p><strong>Pay attention please:</strong> The population always is an integer number. So, a growing of 2.5% over a population of 100 will result in 102 (instead of 102.5) and a growing of 2.5% over a population of 1000 will result in 1025. In addition, use double variables to the growing rate.</p></div>
<h2>Output</h2>
<div>
  <p>
  Print, for each test case, how many years would be necessary to the city A became greater than the city B (in inhabitants). Remember that if this time is greater than 100 it will be necessary printing the message: "Mais de 1 seculo". In each one of these cases, maybe would be interesting interrupt the counting, otherwise you'll get "Time Limit Exceeded".</p>
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
           6<br>
           100 150 1.0 0<br>
           90000 120000 5.5 3.5<br>
           56700 72000 5.2 3.0<br>
           123 2000 3.0 2.0<br>
           100000 110000 1.5 0.5<br>
           62422 484317 3.1 1.0</p>
        </td>
        <td>
          <p>
           51 anos.<br>
           16 anos.<br>
           12 anos.<br>
           Mais de 1 seculo.<br>
           10 anos.<br>
           100 anos.</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>