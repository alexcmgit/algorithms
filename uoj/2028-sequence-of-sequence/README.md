<p><a href="https://www.beecrowd.com.br/repository/UOJ_2028_en.html">beecrowd.com.br/repository/UOJ_2028_en.html</a></p><hr>
<div>
  <span>URI Online | 2028</span>
  <h1>Sequence of Sequence</h1>
  <div>
    <p>By Albertinin Mourato, UFPE <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 3</strong>
</div>
<div>
<div>
  <p>Hyam is a guy that loves sequences. He is finding interesting sequences that even Fibonacci would not have imagined. One day Hyam saw that given a number N, he could make a sequence like 0 1 2 2 3 3 3 4 4 4 …N N N … N. However, Hyam saw that each value that increased in the sequence number, the total quantity increases at a factorial rate. In this case, instead of multiplying, you add the total number of numbers to the sequence with the value of the next number in the sequence. For example, if N = 2. The correct sequence would be 0 1 2 2, which is 4 digits. Now, if N = 3, the next number in the sequence would have the value 3, so the total quantity of numbers in the sequence would bem the quantiy of numbers with N = 2, which is 4, plus the value of the next number in the sequence, in this case 3, giving you 7, since the correct sequence for N = 3 is 0 1 2 2 3 3 3.</p>
  <p>Your task is make an algorithm that given a integer N, has as answer the total quantity of numbers of this sequence and below the complete sequence.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input consists of several test cases. Each case is composed of an integer N (0 &lt;= N &lt;= 200) that indicates the last value of the last N numbers of the sequence numbers.<br>
   The input ends with end of file&nbsp;<strong>(EOF)</strong>.</p>
</div>
<h2>Output</h2>
<div>
  <p>The output is in format <strong>Case X: N numbers</strong>&nbsp;where <strong>X</strong> is the order of number of cases and <strong>N</strong> is the number of numbers that contains the complete sequence, the next line sequence numbers with a space <strong>between</strong> them. You are asked to leave a blank line after each case.</p>
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
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
      </td>
      <td>
        <p>Caso 1: 1 numero</p>
        <p>0</p>
        <br>
        <p>Caso 2: 2 numeros</p>
        <p>0 1</p>
        <br>
        <p>Caso 3: 4 numeros</p>
        <p>0 1 2 2</p>
        <br>
        <p>Caso 4: 7 numeros</p>
        <p>0 1 2 2 3 3 3</p>
        <br>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  </p>
</div>