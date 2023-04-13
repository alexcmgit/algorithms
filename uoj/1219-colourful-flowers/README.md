<p><a href="https://www.beecrowd.com.br/repository/UOJ_1219_en.html">beecrowd.com.br/repository/UOJ_1219_en.html</a></p><hr>
<div>
  <span>URI Online | 1219</span>
  <h1>Colourful Flowers</h1>
  <div><p>
     By Mak Yan Kei <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/hk.gif" style="width: 16px; height: 11px; "> Hong Kong</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
  <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1219_a.jpg" style="width: 190px; height: 132px; float: right; ">"Roses are red, violets are blue..."<br>
  <br>
   Millionaire Mr Smith is well-known -- not for his wealth, but for his odd sense of "art"... Mr Smith has got a circular garden. On the boundary he picks three points and gets a triangle. He then finds the largest circle in that triangular region. So he gets something like this (Please click here for a black-and-white version of the figure):</p>
  <p>
  <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1219_b.png" style="width: 363px; height: 188px; "></p>
  <p>
   Mr Smith then plants yellow sunflowers, blue violets and red roses in the way shown in the figure. (Nice combination, eh? :-) Given the lengths of the three sides of the triangle, you are to find the areas of the regions with each kind of flowers respectively.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   Each line of input contains three integers <strong>a</strong>, <strong>b</strong>, <strong>c</strong>, the lengths of the three sides of the triangular region, with 0 &lt; <strong>a </strong>≤ <strong>b </strong>≤ <strong>c </strong>≤ 1000. The input is terminated by end of file (EOF).&nbsp;</p>
</div>
<h2>Output</h2>
<div>
  <p>
   For each case, your program should output the areas of the regions with sunflowers, with violets and with roses respectively. Print your answers correct to 4 decimal places.</p>
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
          <p>
           3 4 5<br>
           4 30 32</p>
        </td>
        <td>
          <p>
           13.6350 2.8584 3.1416<br>
           954.8794 45.2993 8.2824</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   Tip 1: use for PI: 3.1415926535897 or the constant M_PI of math library<br><br>
   Tip 2: nbsp;https://www.mathopenref.com/heronsformula.html.<br>
  <br>
   A method for calculating the area of a triangle when you know the lengths of all three sides.&nbsp;Let a,b,c be the lengths of the sides of a triangle. The area is given by:<br>
  <br>
  <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1219_c.gif" style="width: 145px; height: 20px; ">&nbsp;where p is half the perimeter, or (a + b + c) / 2</p>
</div>