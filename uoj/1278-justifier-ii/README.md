<p><a href="https://www.beecrowd.com.br/repository/UOJ_1278_en.html">beecrowd.com.br/repository/UOJ_1278_en.html</a></p><hr>
<div>
  <span>URI Online | 1278</span>
  <h1>Justifier II </h1>
  <div><p>
     By Bruno Santos <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px;"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
  We have some texts and we want to right justify them, that is, align them to the right. Create a program that reads a text, formats it right justifies all of its lines, printing them in the same order as they appear in the input.</p>
</div>
<h2>Input</h2>
<div>
  <p>
  The input contains several test cases. The first line of a test case will contain an integer <strong>N</strong> (1 ≤ <strong>N</strong> ≤ 100) indicating the number of lines that form the text. Each of the following <strong>N</strong> lines will contain a text, composed of 1 to 50 uppercase letters (‘A’-‘Z’) or spaces (‘ ’). All text lines will contain at least one letter. There may be more than one space character between words. Also, there may be leading and trailing spaces in the input lines. The end of input is indicated by <strong>N</strong> = 0.</p>
</div>
<h2>Output</h2>
<div>
  <p>
  For each test case print the text lines with a single space character between words, and padded on the left with space characters so that all the lines will have the same length as the longest line existing in that text. Print an empty line between all the test cases. There must be no trailing spaces printed out, and you should discard any unnecessary leading spaces, so that at least one line on every text starts with a letter.</p>
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
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ROMEO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JULIET&nbsp;WERE&nbsp;&nbsp;<br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IN LOVE&nbsp;&nbsp;&nbsp;&nbsp;<br>
           4<br>
           WHO<br>
           ELSE<br>
           LOVES<br>
           STAIRS<br>
           3<br>
           A TEXT CAN BE JUSTIFIED<br>
           ON&nbsp;&nbsp;&nbsp;BOTH&nbsp;&nbsp;&nbsp;SIDES&nbsp;&nbsp;&nbsp;&nbsp;OR<br>
           JUST&nbsp;&nbsp;&nbsp;TO&nbsp;&nbsp;&nbsp;THE&nbsp;&nbsp;&nbsp;RIGHT<br>
           0</p>
        </td>
        <td>
          <p>
           &nbsp;&nbsp;ROMEO AND<br>
           JULIET WERE<br>
           &nbsp;&nbsp;&nbsp;&nbsp;IN LOVE<br>
          <br>
           &nbsp;&nbsp;&nbsp;WHO<br>
           &nbsp;&nbsp;ELSE<br>
           &nbsp;LOVES<br>
           STAIRS<br>
          <br>
           A TEXT CAN BE JUSTIFIED<br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ON BOTH SIDES OR<br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JUST TO THE RIGHT</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>