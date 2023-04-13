<p><a href="https://www.beecrowd.com.br/repository/UOJ_1110_en.html">beecrowd.com.br/repository/UOJ_1110_en.html</a></p><hr>
<div>
  <span>URI Online | 1110</span>
  <h1>Throwing Cards Away</h1>
  <div><p>Folklore, adapted by Piotr Rudnicki <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/ca.gif" style="width: 16px; height: 11px; "> Canada</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   Given in an ordered deck of <em>n</em> cards numbered 1 to <em>n</em> with card 1 at the top and card <em>n</em> at the bottom.<img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1110.jpg" style="width: 232px; height: 308px; float: right;"> The following operation is performed as long as there are at least two cards in the deck:</p>
  <p>
   Throw away the top card and move the card that is now on the top of the deck to the bottom of the deck.</p>
  <p>
   Your task is to find the sequence of discarded cards and the last, remaining card.</p>
  <p>
   Each line of input (except the last) contains a number <em>n</em>&nbsp;≤&nbsp;50. The last line contains 0 and this line should not be processed. For each number from the input produce two lines of output. The first line presents the sequence of discarded cards, the second line reports the last remaining card.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input file contains a non determinated number of lines. Each line contains an integer number. The last line contain the number zero (0).</p>
</div>
<h2>Output</h2>
<div>
  <p>
  For each test case, print two lines. The first line presents the sequence of discarded cards, each number separated by a comma ',' and one blank space. The second line reports the last remaining card. No line will have leading or trailing spaces. See the sample for the expected format.</p>
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
          <p>
           7<br>
           19<br>
           10<br>
           6<br>
           0</p>
        </td>
        <td>
          <p>
           Discarded cards: 1, 3, 5, 7, 4, 2<br>
           Remaining card: 6<br>
           Discarded cards: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14<br>
           Remaining card: 6<br>
           Discarded cards: 1, 3, 5, 7, 9, 2, 6, 10, 8<br>
           Remaining card: 4<br>
           Discarded cards: 1, 3, 5, 2, 6<br>
           Remaining card: 4</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   Formatted by Neilor Tonin</p>
</div>