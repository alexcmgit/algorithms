<p><a href="https://www.beecrowd.com.br/repository/UOJ_1193_en.html">beecrowd.com.br/repository/UOJ_1193_en.html</a></p><hr>
<div>
  <span>URI Online | 1193</span>
  <h1>Base Conversion</h1>
  <div><p>
     By Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 3</strong>
</div>
<div>
<div>
  <p>
   The Julian math teacher has marked a test whose content will be on converting between decimal, hexadecimal and binary numbers. For Julian, this kind of convertion is one of the most complex things to be done. Regardless of the time spent for studying these contents, he simple doesn't understand. So, as you understand about computing and being a friend of Julian, he asked for your help to make a program that checks if the conversions made ​​by him are correct.</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input contains many test cases. The first line of input contains an integer N indicating the number of test cases that follow, one by line. Each test case contains a number X (X &gt; 0) followed by a Y text with three characters, indicating if the X number is in binary, decimal or hexadecimal. Regardless of the format, any of the numbers must fit into a 32-bit integer.</p>
</div>
<h2>Output</h2>
<div>
  <p>
  For each test case, Julian wants that you print the number of the test case folloed by two lines, that contains the oiginal number converted for each one of the other two bases. The sequence of the bases of output is always: decimal, hexadecimal (lowercase) and binary, ie must respect this order obviously excluding the input format.</p>
  <p><br>
   Note: should print a blank line after each test case, even after the last test case.</p>
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
           3<br>
           101 bin<br>
           101 dec<br>
           8f hex</p>
        </td>
        <td>
          <p>
           Case 1:<br>
           5 dec<br>
           5 hex<br>
          <br>
           Case 2:<br>
           65 hex<br>
           1100101 bin<br>
          <br>
           Case 3:<br>
           143 dec<br>
           10001111 bin<br><br></p>
        </td>
      </tr>
    </tbody>
  </table>
</div>