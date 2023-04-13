<p><a href="https://www.beecrowd.com.br/repository/UOJ_1024_en.html">beecrowd.com.br/repository/UOJ_1024_en.html</a></p><hr>
<div>
  <span>URI Online | 1024</span>
  <h1>Encryption</h1>
  <div><p>
     By Neilor Tonin, URI <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; "> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>
  You have been asked to build a simple encryption program. This program should be able to send coded messages without someone been able to read them. The process is very simple. It is divided into two parts. <br><br>
  First, each uppercase or lowercase letter must be shifted three positions to the right, according to the ASCII table: letter 'a' should become letter 'd', letter 'y' must become the character '|' and so on. Second, each line must be reversed. After being reversed, all characters from the half on (truncated) must be moved one position to the left in ASCII. In this case, 'b' becomes 'a' and 'a' becomes '`'. <br><br>
  For example, if the resulting word of the first part is "tesla", the letters "sla" should be moved one position to the left. However, if the resulting word of the first part is "t#$A", the letters "$A" are to be displaced.</p>
</div>
<h2>Input</h2>
<div>
  <p>
  The input contains a number of cases of test. The first line of each case of test contains an integer <strong>N </strong>(1 ≤ <strong>N </strong>≤ 1 * 10⁴), indicating the number of lines the problem should encrypt. The following <strong>N </strong>lines contain <strong>M </strong>characters each <strong>M </strong>(1 ≤<strong>M </strong>≤ 1 * 10³).<br> </p>
</div>
<h2>Output</h2>
<div>
  <p>
   For each input, you must present the encrypted message.</p>
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
           4<br>
           Texto #3<br>
           abcABC1<br>
           vxpdylY .ph<br>
           vv.xwfxo.fd</p>
        </td>
        <td>
          <p>
           3# rvzgV<br>
           1FECedc<br>
           ks. \n{frzx<br>
           gi.r{hyz-xx</p>
        </td>
      </tr>
    </tbody>
  </table>
</div>