<p><a href="https://www.beecrowd.com.br/repository/UOJ_1091_en.html">beecrowd.com.br/repository/UOJ_1091_en.html</a></p><hr>
    <div>
    <span>URI Online | 1091</span>
    <h1>Division of Nlogonia</h1>
    <div><p>
       By Ricardo Anido&nbsp;<img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px;">&nbsp;Brazil</p></div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
       After centuries of hostilities and skirmishes between the four nations living in the land generally known as Nlogonia, and years of negotiations involving diplomats, politicians and the armed forces of all interested parties, with mediation by UN, NATO, G7 and SBC, it was at last agreed by all the way to end the dispute, dividing the land into four independent territories.</p>
      <p>
       It was agreed that one point, called <i>division point</i>, with coordinates established in the negotiations, would define the country division, in the following way. Two lines, both containing the division point, one in the North-South direction and one in the East-West direction, would be drawn on the map, dividing the land into four new countries. Starting from the Western-most, Northern-most quadrant, in clockwise direction, the new countries will be called Northwestern Nlogonia, Northeastern Nlogonia, Southeastern Nlogonia and Southwestern Nlogonia.</p>
      <p>
      <br> <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1091.png" style="width: 501px; height: 237px;"></p>
      <p>
       The UN determined that a page in the Internet should exist so that the inhabitants could check in which of the countries their homes are. You have been hired to help implementing the system.</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>
       The input contains several test cases. The first line of a test case contains one integer <strong><i>K</i> </strong>indicating the number of queries that will be made (<i>0 &lt; <strong>K </strong>≤ 10<sup>3</sup></i>). The second line of a test case contains two integers <strong><i>N</i> </strong>and <strong><i>M</i> </strong>representing the coordinates of the division point (<i>-10<sup>4</sup> &lt; <strong>N</strong>, <strong>M </strong>&lt; 10<sup>4</sup></i>). Each of the <i>K</i> following lines contains two integers <strong><i>X</i> </strong>and <strong><i>Y</i> </strong>representing the coordinates of a residence (<i>-10<sup>4</sup> ≤ <strong>X</strong>, <strong>Y </strong>≤ 10<sup>4</sup></i>).</p>
      <p>
       The end of input is indicated by a line containing only the number zero.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
       For each test case in the input, your program must print one line containing:</p>
      <ul>
        <li>
         the word <font face="courier">divisa</font> (means border in Portuguese) if the residence is on one of the border lines (North-South or East-West);</li>
        <li>
        <font face="courier">NO</font> (means NW in Portuguese) if the residence is in Northwestern Nlogonia;</li>
        <li>
        <font face="courier">NE</font> if the residence is in Northeastern Nlogonia;</li>
        <li>
        <font face="courier">SE</font> if the residence is in Southeastern Nlogonia;</li>
        <li>
        <font face="courier">SO</font> (means SW in Portuguese) if the residence is in Southwestern Nlogonia.</li>
      </ul>
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
           3<br>
           2 1<br>
           10 10<br>
           -10 1<br>
           0 33<br>
           4<br>
           -1000 -1000<br>
           -1000 -1000<br>
           0 0<br>
           -2000 -10000<br>
           -999 -1001<br>
           0</p>
        </td>
        <td>
          <p>
           NE<br>
           divisa<br>
           NO<br>
           divisa<br>
           NE<br>
           SO<br>
           SE</p>
        </td>
      </tr>
    </tbody>
  </table> <p>
   Maratona de Programação da SBC 2008.</p>
</div>