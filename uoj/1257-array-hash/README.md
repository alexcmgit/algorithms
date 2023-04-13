<p><a href="https://www.beecrowd.com.br/repository/UOJ_1257_en.html">beecrowd.com.br/repository/UOJ_1257_en.html</a></p><hr>
    <div>
      <span>URI Online | 1257</span>
      <h1>Array Hash</h1>
      <div><p>
         By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
       You will be given many input lines with strings. The value of each character in input is computed as follows:</p>
      <p>
       Value = (Alphabet Position) + (Element of input) + (Position in Element)</p>
      <p>
      All positions are 0-based. 'A' has alphabet position 0, 'B' has alphabet position 1, ... The returned hash is the sum of all character values in input. For example, if input is:</p>
      <p>
       CBA<br>
       DDD</p>
      <p>
       then each character value would be computed as follows:</p>
      <p>
      <span>2 = 2 + 0 + 0 : 'C' in element 0 position 0<br>
       2 = 1 + 0 + 1 : 'B' in element 0 position 1<br>
       2 = 0 + 0 + 2 : 'A' in element 0 position 2<br>
       4 = 3 + 1 + 0 : 'D' in element 1 position 0<br>
       5 = 3 + 1 + 1 : 'D' in element 1 position 1<br>
       6 = 3 + 1 + 2 : 'D' in element 1 position 2</span><br>
      <br>
       The final hash would be 2+2+2+4+5+6 = 21.</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>
      The input contains many test cases. The first line of input contains an integer <strong>N</strong> that indicates the amount of test cases. Each test case begin with an integer <strong>L</strong>
      (1 ≤ <strong>L</strong> ≤ 100) that indicates the quantity of following lines. Each of these <strong>L</strong> lines will contains a string with up to 50 uppercase letters ('A' - 'Z').</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
       For each test case print the hash calculated according to the above explanation.</p>
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
             5<br>
             2<br>
             CBA<br>
             DDD<br>
             1<br>
             Z<br>
             6<br>
             A<br>
             B<br>
             C<br>
             D<br>
             E<br>
             F<br>
             6<br>
             ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
             ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
             ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
             ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
             ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
             ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
             1<br>
             ZZZZZZZZZZ</p>
          </td>
          <td>
            <p>
             21<br>
             25<br>
             30<br>
             4290<br>
             295</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by Neilor for authorized use in URI OJ.<br>
  * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>