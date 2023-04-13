<p><a href="https://www.beecrowd.com.br/repository/UOJ_1243_en.html">beecrowd.com.br/repository/UOJ_1243_en.html</a></p><hr>
    <div>
      <span>URI Online | 1243</span>
      <h1>How Easy </h1>
      <div><p>
         By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
      TopCoder decided to automate the process of assigning levels of difficulty to the problems. TopCoder developers concluded that the difficulty of the problem is related only to average length of the words in the problem statement. If the average length of the words of the statement is less than or equal to 3, the problem difficulty receives 250 points. If the average length of the words of the statement is 4 or 5, the problem difficulty receives 500 points. If the average length of utterance of words is greater than or equal to 6, the problem difficulty receives 1000 points.</p><br>
      <p>
       Definitions:</p><p>
      Symbol: A set of characters linked by spaces from both sides, or at the beginning of the description of the problem, or even the end of the description of the problem.</p><p>
       Word: a symbol that contains only letters a-z or A-Z, and can be finished with a single point.</p><p>
       Word length: number of letters in a word (a point is not a letter).</p><br>
      <p>
       Examples of symbols are words (quotes just to exemplify): "AB", "ab".</p><p>
       Example of symbols that are not words: "ab..", "a.b", ".ab", "a.b.", "a2b.", ".".</p><br>
      <p>
      The average length of the words is given by the sum of the sizes of the utterance of words divided by the number of words, the division is made by integers. If the word count is zero, then the average length of the words is zero.</p><br>
      <p>
      Your task is given the problem statement, compute its classification of difficulty of the problem, which can be 250, 500, or 1000.</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>
      The entry contains several test cases. Each test case is composed of a line containing the statement of a problem, is a string containing between 1 and 50 characters ('A'-'Z','a'-'z','0'-'9', ' ', '.') inclusive. The end of input is determined by EOF.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
      Compute the average length of words in the statement of the problem, and show the classification of the problem, for more details see the example below.</p>
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
             This is a problem statement<br>
             523hi.<br>
             Implement a class H5 which contains some method.<br>
             &nbsp;no9 . wor7ds he8re. hj..</p>
          </td>
          <td>
            <p>
             500<br>
             250<br>
             500<br>
             250</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by Neilor for authorized use in URI OJ.<br>
  * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>