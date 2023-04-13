<p><a href="https://www.beecrowd.com.br/repository/UOJ_1428_en.html">beecrowd.com.br/repository/UOJ_1428_en.html</a></p><hr>
<div>
<span>URI Online | 1428</span>
<h1>Searching for Nessy</h1>
<div>By Ginés García Mateos, UM <img src="https://resources.beecrowd.com.br/gallery/images/flags/es.gif" alt=""> España</div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p><em>The Loch Ness Monster is a mysterious and unidentified animal said to inhabit Loch Ness, a large deep freshwater loch near the city of Inverness in northern Scotland. Nessie is usually categorized as a type of lake monster.</em><br>
  <em>https://en.wikipedia.org/wiki/Loch_Ness_Monster</em></p>
  <p>In July 2003, the BBC reported an extensive investigation of Loch Ness by a BBC team, using 600 separate sonar beams, found no trace of any "sea monster" (i.e., any large animal, known or unknown) in the loch. The BBC team concluded that Nessie does not exist. Now we want to repeat the experiment.</p>
  <p>Given a grid of n rows and m columns representing the loch, 6 ≤ n, m ≤ 10000, find the minimum number s of sonar beams you must put in the square such that we can control every position in the grid, with the following conditions:</p>
  <ul>
    <li>One sonar occupies one position in the grid; the sonar beam controls its own cell and the contiguous cells;</li>
    <li>The border cells do not need to be controlled, because Nessie cannot hide there (she is too big).</li>
  </ul>
  <p>For example,</p>
  <p><img alt="" src="https://resources.beecrowd.com.br/gallery/images/novos/Searching%20for%20Nessy_C.jpg" style="width: 180px; height: 190px; margin-left: 10px; margin-right: 10px;"> <img alt="" src="https://resources.beecrowd.com.br/gallery/images/novos/Searching%20for%20Nessy_A.gif" style="width: 164px; height: 168px; margin: 10px;"><img alt="" src="https://resources.beecrowd.com.br/gallery/images/novos/Searching%20for%20Nessy_C.gif" style="width: 266px; height: 190px; margin-left: 10px; margin-right: 10px;"></p>
  <p>where X represents a sonar, and the shaded cells are controlled by their sonar beams; the last figure gives us a solution.</p>
</div>
<h2>Input</h2>
<div>
  <p>The first line of the input contains an integer, <strong>t</strong>, indicating the number of test cases. For each test case, there is a line with two numbers separated by blanks, 6 ≤ <strong>n</strong>, <strong>m</strong> ≤ 10000, that is, the size of the grid (<strong>n</strong> rows and <strong>m</strong> columns).</p>
</div>
<h2>Output</h2>
<div>
  <p>For each test case, the output should consist of one line showing the minimum number of sonars that verifies the conditions above.</p>
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
          <p>3<br>
           6 6<br>
           7 7<br>
           9 13</p>
        </td>
        <td>
          <p>4<br>
           4<br>
           12</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Olimpiadas Murcianas de Programación 2009.</p>
</div>