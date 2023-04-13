<p><a href="https://www.beecrowd.com.br/repository/UOJ_2708_en.html">beecrowd.com.br/repository/UOJ_2708_en.html</a></p><hr>
<div>
  <span>URI Online | 2708</span>
  <h1>Tourists in the Huacachina Park</h1>
  <div>
    <p>By André Marcos Silva <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>The municipal tourism agency of the city of Ica in Peru has set up a checkpoint for adventure jeeps that ascend to the dunes of Hucachina Park. As during the day, there are several off-roads that go up and down the national park, and tourists do not always use the same transportation for the round trip, the city hall needed to have better control and security over the flow of visitors in the park. Develop a program that receives as input if a jeep is entering or returning from the park and the amount of tourists this vehicle is transporting. At the end of the shift, the program must indicate how many vehicles and tourists are still missing from the adventure.</p>
</div>
<h2>Input</h2>
<div>
  <p>The program must receive successive input pairs. Each pair should indicate the jeep's movement and the amount of tourists it is carrying. The first entry should be "<em>SALIDA</em>" or "<em>VUELTA</em>". "<em>SALIDA</em>" should indicate that the jeep is leaving the center and entering the park; and "<em>VUELTA</em>" that the Jeep is returning from the ride. Immediately following, the program receives an integer <strong>T</strong> (where, 0 &lt;= <strong>T</strong> &lt;=20) indicating the amount of tourists being transported by the jeep. The string "<em>ABEND</em>" should be the end-of-processing indicator.</p>
</div>
<h2>Output</h2>
<div>
  <p>As a goal the program must present two exits, one in each line: the amount of tourists and the amount of jeeps that still need to return from the park.</p>
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
        <p>SALIDA 10<br>
         SALIDA 12<br>
         SALIDA 10<br>
         VUELTA 20<br>
         ABEND</p>
      </td>
      <td>
        <p>12<br>
         2</p>
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
          <p>SALIDA 15<br>
           SALIDA 20<br>
           VUELTA 15<br>
           VUELTA 15<br>
           SALIDA 0<br>
           VUELTA 0<br>
           ABEND</p>
        </td>
        <td>
          <p>5<br>
           0</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  *Amsilva copyright (2017), for use (authorized) in the URI OJ. All rights reserved.</p>
</div>