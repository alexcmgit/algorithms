<p><a href="https://www.beecrowd.com.br/repository/UOJ_1743_en.html">beecrowd.com.br/repository/UOJ_1743_en.html</a></p><hr>
  <div>
    <span>URI Online | 1743</span>
    <h1>Automated Checking Machine</h1>
    <div>
      <p>By Ricardo Anido, UNICAMP <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
    </div>
    <strong>Timelimit: 1</strong>
  </div>
  <div>
  <div>
    <p>The Internet Computer Parts Company (ICPC) is an on-line shop that sells computer parts. Pairs of in-line electrical connectors are among the most popular parts that ICPC sells. However, they are also one of the parts that are returned more often by unsatisfied customers, because due to errors in packaging the connectors sent to the costumers may not be <em>compatible</em>.</p>
    <p>An in-line connector is composed of five connection points, labelled from 1 to 5. Each connection point of a connector can be either a plug or an outlet. We say two connectors are <em>compatible</em> if, for every label, one connection point is a plug and the other connection point is an outlet (in other words, two connectors are compatible if, for every connection point with the same label, a plug and an outlet meet when the two connectors are connected).</p>
    <p>The figure below shows examples of two connectors that are compatible and two connectors that are not compatible.</p>
    <p><img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1743_en.png" style="width: 505px; height: 127px;"></p>
    <p>ICPC is introducing a state-of-the-art Automated Checking Machine (ACM), with an optical checker, which will verify whether the two connectors packaged for a customer are indeed compatible. The com- plex and expensive hardware of the ACM is ready, but they need your help to finish the software.</p>
    <p>Given the descriptions of a pair of in-line connectors, your task is to determine if the connectors are compatible.</p>
  </div>
  <h2>Input</h2>
  <div>
    <p>The first line contains five integers <strong>X<sub>i</sub></strong> (0 ≤ <strong>X<sub>i</sub></strong> ≤ 1 for <strong>i</strong> = 1, 2, . . . , 5), representing the connection points of the first connector in the pair. The second line contains five integers <strong>Y<sub>i</sub></strong> (0 ≤ <strong>Y<sub>i</sub></strong> ≤ 1 for <strong>i</strong> = 1, 2, . . . , 5), representing the connection points of the second connector. In the input, a 0 represents an outlet an a 1 represents a plug.</p>
  </div>
  <h2>Output</h2>
  <div>
    <p>Output a line with a character representing whether the connectors are compatible or not. If they are compatible write the uppercase letter “Y”; otherwise write the uppercase letter “N”.</p>
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
          <p>1 1 0 1 0<br>
           0 0 1 0 1</p>
        </td>
        <td>
          <p>Y</p>
        </td>
      </tr>
    </tbody>
  </table>
  <div></div><table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>1 0 0 1 0<br>
         1 0 1 1 0</p>
      </td>
      <td>
        <p>N</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  ACM/ICPC Latin America Contest 2014.</p>
</div>