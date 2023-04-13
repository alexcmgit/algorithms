<p><a href="https://www.beecrowd.com.br/repository/UOJ_1457_en.html">beecrowd.com.br/repository/UOJ_1457_en.html</a></p><hr>
<div>
<span>URI Online | 1457</span>
<h1>Oracle of Alexandria</h1>
<div>XIV Maratona de Programação IME-USP <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt=""> Brazil</div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>Every Computer Scientist worth his salt knows the book "The Hitchhiker's Guide to the Galaxy" and knows the answer to the fundamental question about life, the universe and everything. But what few know is that the story of Douglas Adams is based on an Egyptian legend, of an oracle located in Eskendereyya (Alexandria). Alexandria today is the largest city of Egypt, with more than 4 million inhabitants. It is in the Nile Delta, and stretches for 32km along the Mediterranean coast. In the past, the city founded in 331 BC by Alexander the Great, was one of the main cities in the world and there was the Lighthouse of Alexandria (one of the 7 Wonders of the Ancient World), the Library of Alexandria (the largest in the ancient world) and other fantastic works. The legend also says that there was the great oracle of Alexandria. The townspeople delivered the oracle small tickets with numbers noted, and received back a number, that would be the answer to a fundamental question of the universe related to the two given numbers.</p>
  <p>In his treatise of 227 AD Cleomenes of Naucratis (who became administrator of Alexandria when Alexander departed for his conquests) reports some results of the oracle:</p>
  <ul>
    <li>Given 8 and&nbsp;1 the oracle returned 40320;</li>
    <li>Given&nbsp;10 and 3, returned 280;</li>
    <li>Given&nbsp;4 and 2, returned 8;</li>
    <li>Given&nbsp;21 and&nbsp;19, returned 42.</li>
  </ul>
  <p>Modern studies realized that what the oracle returned was nothing more than a generalization of the factorial of an integer. As we know,</p>
  <p>N! = N x (N-1) x ... x 1.</p>
  <p>What the oracle returned for the data N and K, was the K-factor of N, in other words,</p>
  <p>N x (N-K) x (N-2K) x (N-3K) x ...,</p>
  <p>in which the product was made while the difference is greater than or equal to 1. We can represent the K-factor of a number for him followed by K exclamations:</p>
  <ul>
    <li>8! = 40320;</li>
    <li>10!!! = 280;</li>
    <li>4!! = 8;</li>
    <li>21!!!!!!!!!!!!!!!!!!! = 42</li>
  </ul>
  <p>They say that when reading about the legend of oracle Eskendereyya, Douglas Adams got his inspiration for his work. Also, in Egypt is the inspiration of the restaurant at the end of the universe, but that's another story ...</p>
  <p>Given the integers N and K your task is determine K-factor of N.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input is composed of several instances. The first line of input contains an integer <strong>T</strong> indicating the number of instances.</p>
  <p>The first (and only) row of each instance contains an integer <strong>N</strong> followed by <strong>K</strong> points exclamation, where 1 ≤ <strong>N</strong> ≤ 100 and 1 ≤ <strong>K</strong> ≤ 20.</p>
</div>
<h2>Output</h2>
<div>
  <p>For each instance print a line containing the <strong>K</strong>-factor of <strong>N</strong>.</p>
  <p>It is guaranteed that no instance in the input has a result greater than 10<sup>18</sup>.</p>
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
          <p>4<br>
           3!<br>
           10!!!<br>
           19!!!!<br>
           4!!</p>
        </td>
        <td>
          <p>6<br>
           280<br>
           65835<br>
           8</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   XIV Maratona de Programação IME-USP 2010.</p>
</div>