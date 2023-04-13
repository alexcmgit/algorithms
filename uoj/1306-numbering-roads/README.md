<p><a href="https://www.beecrowd.com.br/repository/UOJ_1306_en.html">beecrowd.com.br/repository/UOJ_1306_en.html</a></p><hr>
<div>
<span>URI Online | 1306</span>
<h1>Numbering Roads</h1>
<div><p>By Shahriar Manzoor <img src="https://resources.beecrowd.com.br/gallery/images/flags/bd.gif" alt=""> Bangladesh</p></div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p><img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1306.jpg" style="width: 264px; height: 387px; float: right; margin-left:20px;"></p>
  <p>
   In my country, streets don’t have names, each of them are just given a number as name. These numbers are supposed to be unique but that is not always the case. The local government allocates some integers to name the roads and in many cases the number of integers allocated is less that the total number of roads. In that case to make road names unique some single character suffixes are used. So roads are named as 1, 2, 3, 1A, 2B, 3C etc. Of course the number of suffixes is also always limited to 26 (A, B, …, Z). For example if there are 4 roads and 2 different integers are allocated for naming then some possible assignments of names can be:</p>
  <div>
    <table id="roads">
      <tbody>
        <tr>
          <td>
          1, 2, 1A, 2B</td>
        </tr>
        <tr>
          <td>
          1, 2, 1A, 2C</td>
        </tr>
        <tr>
          <td>
          3, 4, 3A, 4A</td>
        </tr>
        <tr>
          <td>
          1, 2, 1B, 1C</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p>
   Given the number of roads (<b>R</b>) and the numbers of integers allocated for naming (<b>N</b>), your job is to determine the minimum number of different suffixes that will be required (of all possible namings) to name the streets assuming that two streets can't have the same names.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input file can contain up to <b>10002</b> lines of inputs. Each line contains two integers <b>R</b> and <b>N</b> (<b>R</b> &lt; 10001, 0 &lt; <b>N</b>). Here <b>R</b> is the total number of streets to be named and <b>N</b> denotes the number of integers allocated for naming. The end of input is determined by '0 0' and must not be processed.</p>
</div>
<h2>Output</h2>
<div>
  <p>
   Each line of input produces one line of output. This line contains the serial of output followed by an integer <b>D</b> which denotes the minimum number of suffixes required to name the streets. If it is not possible to name all the streets print “impossible” instead (without the quotes).</p>
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
           8 5<br>
           100 2<br>
           0 0</p>
        </td>
        <td>
          <p>
           Case 1: 1<br>
           Case 2: impossible</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Special Thanks: Sohel Hafiz. Adapted by Gerson Groth.</p>
</div>