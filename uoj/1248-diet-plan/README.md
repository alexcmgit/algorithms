<p><a href="https://www.beecrowd.com.br/repository/UOJ_1248_en.html">beecrowd.com.br/repository/UOJ_1248_en.html</a></p><hr>
<div>
  <span>URI Online | 1248</span>
  <h1>Diet Plan</h1>
  <div><p>
     Por TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
  The doctor has given you your diet, in which each character corresponds to some food that you should eat. You also know what you have eaten for breakfast and lunch, in which each character corresponds to a type of food that you have already eaten that day. You have decided that you will eat all of the remaining food in your diet during dinner, and you want to print that as a String (sorted in alphabetical order). If you have cheated in anyway (either by eating too much of one type of food, or by eating some food that is not in the dietPlan), you should print the String "CHEATER" (quotes for clarity).</p>
</div>
<h2>Input</h2>
<div>
  <p>
  Input contains several test cases. The first line of input contains an integer <strong>N</strong> that represents the number of test cases. Each test cases is composed by three strings, each of them in a separated line and representing food from diet, breakfast and lunch, respectively. Each string will contain from 0 to 26 ('A'-'Z'), and can be empty.</p>
</div>
<h2>Output</h2>
<div>
  <p>
  For each test case print a string that represents food should eat during your dinner, or the string "CHEATER" if you have cheated during your diet.</p>
</div>
<div></div>
  <table>
    <thead>
      <tr>
        <td>Input Example</td>
        <td>Output Example</td>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>
           5<br>
           ABCD<br>
           AB<br>
           C<br>
           ABEDCS<br>
          <br>
          <br>
           EDSMB<br>
           MSD<br>
           A<br>
          <br>
          <br>
          <br>
           IWANTSODER<br>
           SOW<br>
           RAT</p>
        </td>
        <td>
          <p>
             D<br>
             ABCDES<br>
             CHEATER<br>
            <br>
             DEIN<br>
          </p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by Wisllay Vitrio for authorized use in URI OJ.<br>
   * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>