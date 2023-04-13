<p><a href="https://www.beecrowd.com.br/repository/UOJ_2630_en.html">beecrowd.com.br/repository/UOJ_2630_en.html</a></p><hr>
<div>
  <span>URI Online | 2630</span>
  <h1>Greyscale</h1>
  <div>
    <p>By Edson Alves da Costa Júnior, UNB <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
  <p>Some image processing algorithms require preprocessing in which it is necessary to turn a color image into a greyscale image. This conversion can be done in several ways, depending on the result you want to achieve.</p>
  <p>To preserve the perception of basic colors by the human eye, an appropriate conversion would be to take 30% of the red component (R), 59% of the green component (G) and 11% of the blue component (B). In mathematical terms:</p>
  <p><strong>P</strong> = 0, 30R + 0, 59G + 0, 11B</p>
  <p>Other possible approaches would be to determine the value of <strong>P</strong> through the arithmetic mean of the three components or assign <strong>P</strong> to the highest or the lowest values among the three components.</p>
  <p>Given the RGB components of one pixel of the color image, determine the value of pixel <strong>P</strong> of the corresponding gray scale image, determining the conversion to be used. Neglect the decimal part of the result, if it exists.</p>
</div>
<h2>Input</h2>
<div>
  <p>The input in <strong>T</strong> (1 ≤ <strong>T</strong> ≤ 100) test cases, where the value of <strong>T</strong> is given in the first line of the input. Each test case consists of two lines: the first line contains the conversion to be used: eye for the first approach described, mean for the arithmetic mean, max for the largest component value and min for the lowest component value. The second line contains the <strong>R</strong>, <strong>G</strong>, <strong>B</strong> (0 ≤ <strong>R</strong>, <strong>G</strong>, <strong>B</strong> ≤ 255) values of the colored image pixel.</p>
</div>
<h2>Output</h2>
<div>
  <p>For each test case the following message<em> "Caso #t: P"</em> should be printed, where <strong>P</strong> is the gray level of the pixel of the grayscale image after the conversion of the colored image pixel. This message must be followed by a line break.</p>
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
        <p>3</p>
        <p>min</p>
        <p>35 70 35</p>
        <p>mean</p>
        <p>10 74 181</p>
        <p>eye</p>
        <p>23 78 197</p>
      </td>
      <td>
        <p>Caso #1: 35</p>
        <p>Caso #2: 88</p>
        <p>Caso #3: 74</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  Maratona de Programação UnB/CIC 2015.</p>
</div>