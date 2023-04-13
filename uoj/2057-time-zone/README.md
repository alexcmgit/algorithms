<p><a href="https://www.beecrowd.com.br/repository/UOJ_2057_en.html">beecrowd.com.br/repository/UOJ_2057_en.html</a></p><hr>
<div>
  <span>URI Online | 2057</span>
  <h1>Time Zone</h1>
  <div>
    <p>By Neilor Tonin, URI <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>Paul and Peter have made a long journey since they left Brazil to compete in the ICPC World Finals, in Phuket, Thailand. They noticed that in each place where they stopped, they had to adjust their watches because of the time zone.</p>
  <p>This way, to plan for upcoming trips, they asked you to create a mobile application that, given the departure time, travel time and the destination time zone with respect to the origin, you have to inform the time of arrival of each flight in the destination.</p>
  <p>For example, if they left a place at 10 am for a 4 hour journey to a destination that is on the east, in a time zone with an extra hour with respect to the time zone of the starting point, the arrival time will be 10 hours + 4 hours + 1 hour (due de time zone), i.e. they will arrive at 15 hours. Note that if the calculated time is 24, its program should print 0 (zero).</p>
</div>
<h2>Input</h2>
<div>
  <p>The input contains 3 integers: <strong>S</strong> (0 ≤ <strong>S </strong>≤ 23), <strong>T</strong> (1 ≤ <strong>T</strong> ≤ 12) y <strong>F</strong> (-5 ≤ <strong>F</strong> ≤ 5), separated by a space, respectively indicating the time of departure, the travel time and destination time zone with respect to the origin.</p>
</div>
<h2>Output</h2>
<div>
  <p>Print an integer that indicates the local time specified in destination, as the examples below.</p>
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
        <p>10 7 3</p>
      </td>
      <td>
        <p>20</p>
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
          <p>22 6 -2</p>
        </td>
        <td>
        2</td>
      </tr>
    </tbody>
  </table>
  <table>
    <thead>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>0 3 -4</p>
        </td>
        <td>
        23</td>
      </tr>
    </tbody>
  </table>
  <p>
   Aquecimento para a OBI 2016<br>
  Acknowledgments to Jean Bez</p>
</div>