<p><a href="https://www.beecrowd.com.br/repository/UOJ_1848_en.html">beecrowd.com.br/repository/UOJ_1848_en.html</a></p><hr>
<div>
  <span>URI Online | 1848</span>
  <h1>Counting Crow</h1>
  <div>
    <p>By Emilio Wuerges, UFFS <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>As we know, there's a three-eyed crow. What it isn't well known is that the three-eyed crow can foresaw the results of Westeros lottery. Meanwhile every other crow is flying collecting entries for the lottery, the three-eyed crow already knows the results, and when Bran dreams with the three-eyed crow, the crow tells him the result. Bran always remember these dreams very well, however, he can't understand them fast enough to know the result. Your task is write a program to calculate the result from Bran's dream.</p>
  <p>During the dream, the crow blinks many times and screams exactly 3 times. Every scream corresponds to a result.</p>
  <p>Every blink of the crow communicates a binary number. An open eye means <strong>1</strong> and a closed eye means <strong>0</strong>. The left eye is the <strong>most significative </strong>eye and the right eye is the <strong>least significative </strong>eye. Every blink this number is added and when the crow screams, the <strong>sum </strong>is a result.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input describes, in every line, in order, a scream or a blink of the crow.</p>
  <p>A scream is represented by the string <strong>caw caw</strong>.</p>
  <p>A blink is formed by three characters <strong>*</strong> ou <strong>-</strong>, representing, respectively, an open eye or a closed eye, from left to right.</p>
  <p>Remember that the crow has <strong>3</strong> eyes.</p>
  <p>The winning numbers at lottery do not exceed 1000.</p>
</div>
<h2>Output</h2>
<div>
  <p>The output are 3 lines, each one with one result of the lottery.</p>
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
           --*<br>
           caw caw<br>
           *--<br>
           caw caw<br>
           caw caw<br>
        </td>
        <td>
           1 <br>
           4 <br>
           0 <br>
        </td>
      </tr>
    </tbody>
  </table>
  <div>
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
             --* <br>
             --* <br>
             --* <br>
             caw caw <br>
             *-- <br>
             *-- <br>
             caw caw <br>
             --* <br>
             *-- <br>
             caw caw <br>
          </td>
          <td>
             3 <br>
             8 <br>
             5 <br>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <p>
  Escola de Inverno da Maratona - Erechim RS - 2015</p>
</div>