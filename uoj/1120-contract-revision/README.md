<p><a href="https://www.beecrowd.com.br/repository/UOJ_1120_en.html">beecrowd.com.br/repository/UOJ_1120_en.html</a></p><hr>
<div>
  <span>URI Online | 1120</span>
  <h1>Contract Revision</h1>
  <div><p>Maratona de Programação da SBC <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px;"> Brasil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
   For years, all contracts of the Association of Contracts for Modernization (ACM) were typed using an old typewriter machine.<br>
  <br>
   Recently Mr. Miranda, one of the accountants of the ACM, realized that the machine had a failure in one, and only one, numerical digit. More specifically, the flawed digit, when typed, is not printed on the sheet, as if the corresponding key was not pressed. He realized that this could have changed the numerical representation of contract values. Worried about accounting, Mr. Miranda wants to know, from the original values agreed for the contracts (which he kept in handwritten notes) which values are actually represented in the contracts. For example, if the failed digit in the machine is 5, an agreed value of 1500 would be represented in the corresponding contract as 100, because the digit 5 would not be printed. Note that Mr. Miranda wants to know the numeric value represented in the contract, ie, in the same machine, the number 5000 corresponds to the numeric value 0, not 000 (as it actually appears in the contract).</p>
</div>
<h2>Input</h2>
<div>
  <p>
   The input consists of several test cases, each in one line. Each line contains two integers<strong>D</strong> and <strong>N</strong> (1 ≤ <strong>D</strong> ≤ 9, 1 ≤ <strong>N</strong> &lt; 10<sup>100</sup> ), representing, respectively, the digit that has failed in the machine and the number that was originally agreed for the contract (which can be very large because of hiperinflation).<br>
  <br>
   The last test case is followed by a line which contains only two zeros separated by white space.</p>
</div>
<h2>Output</h2>
<div>
  <p>
   For each test case in the input your program must print one line containing a single integer, the numeric value represented in the contract.</p>
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
           5 5000000<br>
           3 123456<br>
           9 23454324543423<br>
           9 99999999991999999<br>
           7 777<br>
           0 0</p>
        </td>
        <td>
          <p>
           0<br>
           12456<br>
           23454324543423<br>
           1<br>
           0</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
   Maratona de Programação da SBC 2010</p>
</div>