<p><a href="https://www.beecrowd.com.br/repository/UOJ_1250_en.html">beecrowd.com.br/repository/UOJ_1250_en.html</a></p><hr>
    <div>
      <span>URI Online | 1250</span>
      <h1>KiloMan</h1>
      <div><p>
         By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>You've reached one of the last bosses in the new hit 2-D side-scrolling action game, KiloMan. The boss has a large gun that can shoot projectiles at various heights. For each shot, KiloMan can either stand still or jump. If he stands still and the shot is at height 1 or 2, then he gets hit. If he jumps and the shot is at a height above 2, then he is also hit. Otherwise, he is not hit. Given the height of each shot and a sequence of jumps, how many hits will KiloMan take?</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>The input contains several test cases. The first line of input contain an integer <strong>N</strong> that indicates the number of test cases. Each test case is composed by three lines and starts with a line containing the number of shots <strong>S</strong> (1 ≤ <strong>S</strong> ≤ 50). The second line contains <strong>S</strong> integers, that represent the pattern of heights at which the shots are being fired. Each element of pattern will be between 1 and 7, inclusive. The third line of input contains the string 'jumps', that represents the sequence of jumps that KiloMan will attempt; 'J' means he will jump and 'S' means he will stand still. For example, if the first number of the pattern is 3 and the first character of jumps is 'J', then KiloMan will jump right as a shot is fired at height 3 (and thus he will be hit).</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>For each case, your program should print an integer representing the number of times KiloMan is hit.</p>
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
             4<br>
             9<br>
             1 3 2 3 3 1 2 2 1<br>
             JJSSSJSSJ<br>
             49<br>
             1 1 1 1 1 1 1 2 2 2 2 2 2 2 3 3 3 3 3 3 3 4 4 4 4 4 4 4 5 5 5 5 5 5 5 6 6 6 6 6 6 6 7 7 7 7 7 7 7<br>
             SSSSSSSSSSSSSSJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ<br>
             4<br>
             1 2 2 1<br>
             SJJS<br>
             1<br>
             1<br>
             J</p>
          </td>
          <td>
            <p>
             4<br>
             49<br>
             2<br>
             0</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by Julio B. for authorized use in URI OJ.<br>
   * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>