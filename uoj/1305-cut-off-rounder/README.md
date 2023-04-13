<p><a href="https://www.beecrowd.com.br/repository/UOJ_1305_en.html">beecrowd.com.br/repository/UOJ_1305_en.html</a></p><hr>
        <div>
          <span>URI Online | 1305</span>
          <h1>Cut Off Rounder</h1>
          <div><p>
             By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
          </div>
          <strong>Timelimit: 1</strong>
        </div>
        <div>
        <div>
          <p>
           Often, when we round a real valued number to an integer, we round up if the fractional part is 0.5 or greater, and down if the fractional part is less than 0.5. In this problem, you have to write a method round, which takes a real valued number as a String,&nbsp;<strong>num</strong>, and a cutoff as a String,&nbsp;<strong>cutoff</strong>.&nbsp;<strong>cutoff</strong>&nbsp;will be formatted exactly as&nbsp;<span>"0.####"</span>, where each&nbsp;<span>'#'</span>&nbsp;represents a digit ('0'-'9'). At least one of the digits to the right of the decimal point in&nbsp;<strong>cutoff</strong>&nbsp;will be non-zero. Your task is to round&nbsp;<strong>num</strong>&nbsp;up if its fractional part is greater than cutoff, and down otherwise, and return the result as an int. To avoid issues with double imprecision, the fractional part of&nbsp;<strong>num</strong>&nbsp;will not be exactly equal to&nbsp;<strong>cutoff</strong>. Hence, the traditional rounding method described in the opening sentence would be represented by&nbsp;cutoff = "0.5000".</p>
        </div>
        <h2>Input</h2>
        <div>
        <p>
         The input contains several test cases.&nbsp;Each one is given in two lines. The <strong>num</strong> string is at the first line and the <strong>cutoff</strong>&nbsp;is at the second line.&nbsp;<strong>num</strong> will be a sequence of one or more digits ('0'-'9'), with an optional decimal point ('.').&nbsp;<strong>num</strong> will contain between 1 and 10 characters, inclusive.&nbsp;<strong>cutoff </strong>will be formatted exactly as "0.####", where each '#' represents a digit ('0'-'9'). The fractional part of <strong>num</strong> will NOT be exactly equal to <strong>cutoff</strong>. <br> <br>
      </p><p>The input is terminatted by EOF.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
       Your program should output one line to&nbsp;each test case. This line contains only the integer part of <strong>num</strong> rounded up or down according to the given <strong>cutoff</strong>.</p>
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
             003.656930<br>
             0.5000<br>
             .001<br>
             0.0001<br>
             1.99999999<br>
             0.9999<br>
             135<br>
             0.6531<br>
             135.<br>
             0.6531<br>
             1356.13671<br>
             0.1367<br>
             0.00010001<br>
             0.0001</p>
          </td>
          <td>
            <p>
             4<br>
             1<br>
             2<br>
             135<br>
             135<br>
             1357<br>
             1</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by M. C. Pinto for authorized use in URI OJ.<br>
   * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>