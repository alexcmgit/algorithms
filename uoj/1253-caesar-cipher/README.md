<p><a href="https://www.beecrowd.com.br/repository/UOJ_1253_en.html">beecrowd.com.br/repository/UOJ_1253_en.html</a></p><hr>
    <div>
      <span>URI Online | 1253</span>
      <h1>Caesar Cipher </h1>
      <div><p>
         By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
      Julius Caesar used a system of cryptography, now known as Caesar Cipher, which shifted each letter 2 places further through the alphabet (e.g. 'A' shifts to 'C', 'R' shifts to 'T', etc.). At the end of the alphabet we wrap around, that is 'Y' shifts to 'A'. We can, of course, try shifting by any number.</p>
    </div>
    <h2>Input</h2>
    <div>
      <p>
      The input contains several test cases. The first line of input contains an integer <strong>N </strong> that indicates the number of test cases. Each test case is composed by two lines. The first line contais a string that is a codified sentence. This string will contain between 1 and 50 characters, inclusive. Each character is an uppercase letter ('A'-'Z'), that is the codified sentence to this modified Caesar Cipher. The second line contains the number of right shift, this value is between 0 and 25, inclusive.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
       Given an encoded text and a number of shifted letters, decode it to the original sentence, acording to the explanation above and the following example.</p>
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
             6<br>
             VQREQFGT<br>
             2<br>
             ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
             10<br>
             TOPCODER<br>
             0<br>
             ZWBGLZ<br>
             25<br>
             DBNPCBQ<br>
             1<br>
             LIPPSASVPH<br>
             4</p>
          </td>
          <td>
            <p>
             TOPCODER<br>
             QRSTUVWXYZABCDEFGHIJKLMNOP<br>
             TOPCODER<br>
             AXCHMA<br>
             CAMOBAP<br>
             HELLOWORLD</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by Vanessa Leite for authorized use in URI OJ.<br>
   * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>