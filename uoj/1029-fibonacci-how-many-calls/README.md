<p><a href="https://www.beecrowd.com.br/repository/UOJ_1029_en.html">beecrowd.com.br/repository/UOJ_1029_en.html</a></p><hr>
    <div>
      <span>URI Online | 1029</span>
      <h1>Fibonacci, How Many Calls?</h1>
      <div><p>
         By Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
    <p>
     Sometimes when you are a Computer Science student, you’ll see an exercise or a problem involving the Fibonacci sequence. This sequence has the first two values 0 (zero) and 1 (one) and each next value will always be the sum of the two preceding numbers. By definition, the formula to find any Fibonacci number is:<br>
    <span>
     fib(0) = 0<br>
     fib(1) = 1<br>
     fib(n) = fib(n-1) + fib(n-2);</span></p><p>
     One way of finding Fibonacci numbers is by recursive calls. This is illustrated below, presenting the tree of derivation when we calculate fib(4), i.e. the fifth value of this sequence:</p>
    <br> <p>
    <img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1029.png" style="width: 468px; height: 265px;"></p>
    <br>
    In this way,<ul>
    <li>
     fib(4) = 1+0+1+1+0 = 3</li>
    <li>
     8 recursive calls were done.</li>
  </ul>
</div>
<h2>Input</h2>
<div>
  <p>
   The first input line contains a single integer <strong>N</strong>, indicating the number of test cases. Each test case contains an integer number <strong>X</strong> (1 ≤ <strong>X</strong> ≤ 39) .</p>
</div>
<h2>Output</h2>
<div>
  <p>
   For each test case we will have an output line, in the following format: fib(n) = <strong>num_calls</strong> calls = <strong>result</strong>, where num_calls is the number of recursive calls, always with a space before and after the equal sign, as shown below.</p>
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
           2<br>
           5<br>
           4</p>
        </td>
        <td>
          <p>
           fib(5) = 14 calls = 5<br>
           fib(4) = 8 calls = 3</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>