<p><a href="https://www.beecrowd.com.br/repository/UOJ_1273_en.html">beecrowd.com.br/repository/UOJ_1273_en.html</a></p><hr>
    <div>
      <span>URI Online | 1273</span>
      <h1>Justifier </h1>
      <div><p>
         By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
      We have some words and we want to right justify them, that is, align them to the right. Create a program that reads a word and print it all right justified, in the same order as they appear in the input.</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>
       The input contains several test cases. The first line of a test case will contain an integer <strong>N</strong> (1 ≤ <strong>N</strong> ≤ 50) indicating the number of following words. Each word is composed of up to 50 uppercase letters (‘A’-‘Z’) and will contain at least one letter. The end of input is indicated by <strong>N</strong> = 0.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
      For each test case print the words padded on the left with space characters so that they are all the same length as the longest word found in that text. Print an empty line between all the test cases. There must be no trailing spaces printed out, and you should discard any unnecessary leading spaces, so that at least one line on every output word starts with a letter.</p>
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
             3<br>
             BOB<br>
             TOMMY<br>
             JIM<br>
             4<br>
             JOHN<br>
             JAKE<br>
             ALAN<br>
             BLUE<br>
             4<br>
             LONGEST<br>
             A<br>
             LONGER<br>
             SHORT<br>
             0</p>
          </td>
          <td>
            <p>
             &nbsp;&nbsp;BOB<br>
             TOMMY<br>
             &nbsp;&nbsp;JIM<br>
            <br>
             JOHN<br>
             JAKE<br>
             ALAN<br>
             BLUE<br>
            <br>
             LONGEST<br>
             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A<br>
             &nbsp;LONGER<br>
             &nbsp;&nbsp;SHORT</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by bitfreeze for authorized use in URI OJ.<br>
   * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>