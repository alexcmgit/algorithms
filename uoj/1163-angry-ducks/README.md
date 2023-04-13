<p><a href="https://www.beecrowd.com.br/repository/UOJ_1163_en.html">beecrowd.com.br/repository/UOJ_1163_en.html</a></p><hr>
<div>
  <span>URI Online | 1163</span>
  <h1>Angry Ducks</h1>
  <div><p>
     by Marcelo Luiz Onhate <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   In a far away land there are two cities, Nlogony, home of the Nlogonies, and Ducklogony, home of their neighbors, the Ducknese. These two cities have been at war for some time and now, in a try to win the war, the Ducknese intend to attack Nlogony with a slingshot that fires ducks. However, to avoid mistakes, they asked you to build a program that, given the values of the slingshot's height (<strong>h</strong>), the points where the Nlogony city begins (<strong>p1</strong>) and ends (<strong>p2</strong>), the shooting angle (<strong>α</strong>) and the launching speed, calculates if the projectile will hit the target.</p> <br>
  <p>
  <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1163.jpg" style="text-align: center; width: 674px; height: 319px; "></p>
  <p> <br>
   For the calculations, assume that the gravity's acceleration is g=9,80665 and that π = 3,14159. </p>
  <h2>Input</h2>
  <div>
    <p>
     There are various test cases, where each one starts with 1 floating point value <strong>h</strong>( 1 ≤ <strong>h</strong> ≤ 150) indicating the slingshot's height, containing, in the next line, 2 integer values <strong>p1</strong> and <strong>p2</strong>( 1 ≤ <strong>p1, p2</strong> ≤ 9999) indicating where Nlogony begins and ends, the next line containing 1 integer <strong>n</strong>(1 ≤ <strong>n</strong> ≤ 100) indicating the number of tries that will be made to hit the Nlogony and the <strong>n</strong> following lines containing 2 floating point values indicating the values of the launching's angle <strong>α</strong>(1 ≤ <strong>α</strong> ≤ 180) and speed <strong>V</strong>(1 ≤ <strong>V </strong>≤ 150).<br>
    <br>
     The end of the input file is determined by EOF.</p>
  </div>
  <h2>Output</h2>
  <div>
    <p>
     For each shoot, your program must print a single line in the following format: “X -&gt; DUCK” for when the duck hits Nlogony or “X -&gt; NUCK” where the duck doesn't hit Nlogony, where <strong>X</strong> is the maximum distance that the projectile reached until reaching the ground (y = 0). X must be printed with an accuracy of 5 decimal places.</p>
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
             2.1<br>
             368 380<br>
             3<br>
             42.3 60<br>
             30 55<br>
             44 60.876842</p>
          </td>
          <td>
            <p>
             367.76208 -&gt; NUCK<br>
             270.72675 -&gt; NUCK<br>
             379.83781 -&gt; DUCK</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
     Acknowledgments to Éber Jessé da Silva Peretto by the translation.</p>
  </div>
</div>