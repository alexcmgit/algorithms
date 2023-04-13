<p><a href="https://www.beecrowd.com.br/repository/UOJ_1262_en.html">beecrowd.com.br/repository/UOJ_1262_en.html</a></p><hr>
    <div>
      <span>URI Online | 1262</span>
      <h1>Multiple Reading </h1>
      <div><p>
         By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
      In many computer systems, multiple processes can read from the same resource during the same clock cycle, but only a single process can write to the resource during a clock cycle. Reads and writes cannot be mixed during the same clock cycle. Given a history of the reads and writes that occurred during a particular computation as a String <b>trace</b>, and an int <b>procs</b> representing the number of processes used by the computation, calculate the minimum duration of the computation in clock cycles. The <b>trace</b>
       represents each read as an 'R' and each write as a 'W'.</p>
      <p>
      For example, if <b>trace</b> is "<span>RWWRRR</span>" and <b>procs</b> is 3, then the minimum number of clock cycles is 4: one for the first read, one each for the two writes, and one for the last group of reads.</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>
      The input contains several test cases. Each test case is composed by two lines. The first line has a string made out of 1 to 50 characters, where each can be either 'R' or 'W'. The second line contains an integer <strong>P&nbsp;</strong>(1 ≤&nbsp;<strong>P&nbsp;</strong>≤ 10), which represents the number of processes as a direct indicator of how many read operations can be performed simultaneously. The input stream ends in EOF.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
       For each test case determine and print the minimum number of clock cycles required to run the given <b>trace</b>. For further reference see the examples below.</p>
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
             RWWRRR<br>
             3<br>
             RWWRRRR<br>
             3<br>
             WWWWW<br>
             5<br>
             RRRRRRRRRR<br>
             4<br>
             RWRRWWRWRWRRRWWRRRRWRRWRRWRRRRRRRRRWRWRWRRRRWRRRRR<br>
             4</p>
          </td>
          <td>
            <p>
             4<br>
             5<br>
             5<br>
             3<br>
             30</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by bitfreeze for authorized use in URI OJ.<br>
   * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>