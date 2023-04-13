<p><a href="https://www.beecrowd.com.br/repository/UOJ_1026_en.html">beecrowd.com.br/repository/UOJ_1026_en.html</a></p><hr>
  <div>
    <span>URI Online | 1026</span>
    <h1>To Carry or not to Carry</h1>
    <div><div>
      <p>
       By Monirul Hasan Tomal, SEU <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/bd.gif" style="width: 16px; height: 11px;"> Bangladesh</p>
    </div>
  </div>
  <strong>Timelimit: 2</strong>
</div>
<div>
<div>
  <p>
  <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1026.png" style="width: 273px; height: 178px; float: left;">6+9=15 seems okay. But how come 4+6=2?<br>
  <br>
   Look at, Mofiz worked hard throughout his Digital Logic course, but when he was asked to implement a 32 bit adder for the laboratory exam, he did some mistake in the design part. After scavenging the design for half an hour, he found his flaw!! He was doing bitwise addition but his carry bit always had zero output. Thus,</p><p>
  <br>
  <span>4&nbsp; = 00000000 00000000 00000000 00000100<br>
   +6 = 00000000 00000000 00000000 00000110<br>
   ----------------------------------------<br>
   2&nbsp; = 00000000 00000000 00000000 00000010</span><br>
  <br>
   It’s a good thing that he finally found his mistake, but it was too late. Considering his effort throughout the course, the instructor gave him one more chance. Mofiz had to write an efficient program that would take 2 unsigned 32 bit decimal numbers as input, and produce an unsigned 32 bit decimal number as the output adding in the same way as his circuit does.</p>
  <p>
  </p>
</div>
<h2>Input</h2>
<div>
  <p>
   In each input line there will be a pair of integer separated by a single space. Input ends at EOF.</p>
</div>
<h2>Output</h2>
<div>
  <p>
   For each input line, the program must provide an output's line: the value after adding the two numbers in the "Mofiz way".</p>
</div>
<div></div>
  <table>
    <thead>
      <tr>
        <td>Input Sample</td>
        <td>Output Sample</td>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>
           4 6<br>
           6 9</p>
        </td>
        <td>
          <p>
           2<br>
           15</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>