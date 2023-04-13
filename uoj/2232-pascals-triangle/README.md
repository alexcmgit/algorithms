<p><a href="https://www.beecrowd.com.br/repository/UOJ_2232_en.html">beecrowd.com.br/repository/UOJ_2232_en.html</a></p><hr>
<div>
  <span>URI Online | 2232</span>
  <h1>Pascal's Triangle</h1>
  <div>
    <p>By Gabriel Taets, Universidade Federal de Itajubá <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>Pascal's Triangle (also known as Tartaglia Triangle in some countries), is an infinite numeric triangle formed by binomial numbers <img alt="Binomial" src="https://www.urionlinejudge.com.br/gallery/images/contests/UOJ_2232_b.png" style="height:24px; width:22px">, where <strong>n</strong> represents the row number and <strong>k</strong> represents the column number (0-indexed). The triangle was discovered by the chinese mathematician Yang Hui, and 500 years later, many of its properties was studied by Blaise Pascal. Each number in Pascal's Triangle is equal to the sum of the number immediately above it and its predecessor.</p>
  <p style="text-align:center"><img alt="Pascal's Triangle" src="https://www.urionlinejudge.com.br/gallery/images/contests/UOJ_2232_a.png" style="height:204px; width:491px"></p>
  <p>David, the mastermind of your competitive programming team, found that the sum of the <strong>i</strong><strong><sub>th</sub></strong> row of the Pascal's Triangle is <strong>2<sup>i</sup></strong>. Now, he wants to find the sum of the first N rows of the triangle. However, he thinks this problem is too easy and does not deserve his attention (he decided to try to solve a problem about bipartite graphs instead, a much harder topic), thus, you are the one who must solve this problem.</p>
</div>
<h2>Input</h2>
<div>
  <p>First line of input contains an integer <strong>T</strong>, the number of test cases. The next <strong>T</strong> lines contain a number <strong>N</strong> (1 ≤ <strong>N</strong> ≤ 31), the number of lines in the Pascal's Triangle you must solve.</p>
</div>
<h2>Output</h2>
<div>
  <p>For each test case, the output must contain a line with an integer <strong>S</strong>, the sum of the first <strong>N</strong> lines in the Pascal's Triangle.</p>
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
        <p>4<br>
         1<br>
         2<br>
         5<br>
         31</p>
      </td>
      <td>
        <p>1<br>
         3<br>
         31<br>
         2147483647</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  </p>
</div>