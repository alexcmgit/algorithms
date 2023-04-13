<p><a href="https://www.beecrowd.com.br/repository/UOJ_1847_en.html">beecrowd.com.br/repository/UOJ_1847_en.html</a></p><hr>
<div>
  <span>URI Online | 1847</span>
  <h1>Welcome to the Winter!</h1>
  <div>
    <p>By Leandro Zatesko, UFFS <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
<div>
<p>Welcome to the Erechim Winter School of the ICPC Brazilian Subregional Contest! We sincerely hope you learn a lot during these days so you can be very successful in the Programming contests yet to come, but above all we hope you enjoy the School, for when we have fun and enjoy ourselves studying and programming, the training stops being a burden and becomes a hobby. So, have fun!</p>
<p>The winter is a wonderful season, is it not? We all love wearing a poncho, joining a <em>chimarrão</em> circle, baking <em>pinhões</em> in a wooden burning stove… But not everyone likes the winter, especially in places where winter uses to be very cruel. In Westeros, for example, the people's humour is defined according to climate tendencies. Based on the temperatures of the last three days, the people can be sad or happy, being more likely to make war or to make love, respectively. And, let us be honest, it is precisely because of the scenes of love and war that we love Game of Thrones!</p>
<ul>
  <li>If the temperature decreased from the 1<sup>st</sup> to the 2<sup>nd</sup> day, but increased or remained constant from the 2<sup>nd</sup> to the 3<sup>rd</sup>, the people are happy (first figure).</li>
  <li>If the temperature increased from the 1<sup>st</sup> to the 2<sup>nd</sup> day, but decreased or remained constant from the 2<sup>nd</sup> to the 3<sup>rd</sup>, the people are sad (second figure).</li>
  <li>If the temperature increased from the 1<sup>st</sup> to the 2<sup>nd</sup> day and from the 2<sup>nd</sup> to the 3<sup>rd</sup>, but increased from the 2<sup>nd</sup> to the 3<sup>rd</sup> less than what had increased from the 1<sup>st</sup> to the 2<sup>nd</sup>, the people are sad (third figure).</li>
  <li>If the temperature increased from the 1<sup>st</sup> to the 2<sup>nd</sup> day and from the 2<sup>nd</sup> to the 3<sup>rd</sup>, but increased from the 2<sup>nd</sup> to the 3<sup>rd</sup> at least what had increased from the 1<sup>st</sup> to the 2<sup>nd</sup>, the people are happy (fourth figure).</li>
  <li>If the temperature decreased from the 1<sup>st</sup> to the 2<sup>nd</sup> day and from the 2<sup>nd</sup> to the 3<sup>rd</sup>, but decreased from the 2<sup>nd</sup> to the 3<sup>rd</sup> less than what had decreased from the 1<sup>st</sup> to the 2<sup>nd</sup>, the people are happy (fifth figure).</li>
  <li>If the temperature decreased from the 1<sup>st</sup> to the 2<sup>nd</sup> day and from the 2<sup>nd</sup> to the 3<sup>rd</sup>, but decreased from the 2<sup>nd</sup> to the 3<sup>rd</sup> at least what had decreased from the 1<sup>st</sup> to the 2<sup>nd</sup>, the people are sad (sixth figure).</li>
  <li>If the temperature remained constant from the 1<sup>st</sup> to the 2<sup>nd</sup> day, the people are happy if the temperature increased from the 2<sup>nd</sup> to the 3<sup>rd</sup> or sad otherwise (respectively, seventh and eighth figures).</li>
</ul>
<p>
<img alt="" src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1847.jpg" style="width: 547px; height: 266px;"></p> </div>
<h2>Input</h2>
<div>
  <p>The input consists only of three integers, <strong>A</strong>, <strong>B</strong> e <strong>C</strong> (-100 ≤ <strong>A</strong>, <strong>B</strong>, <strong>C</strong> ≤ 100), which represent respectively the temperatures recorded in the 1<sup>st</sup>, in the 2<sup>nd</sup> and in the 3<sup>rd</sup> day.</p>
</div>
<h2>Output</h2>
<div>
  <p>Print a line containing a happy or a sad smiley, representing how is the humour of the people of Westeros according to the climate tendencies.</p>
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
        <p>20 10 12</p>
      </td>
      <td>
        <p>:)</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>10 20 18</p>
      </td>
      <td>
        <p>:(</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>4 16 20</p>
      </td>
      <td>
        <p>:(</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>4 10 20</p>
      </td>
      <td>
        <p>:)</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>20 10 6</p>
      </td>
      <td>
        <p>:)</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>20 16 4</p>
      </td>
      <td>
        <p>:(</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>10 10 14</p>
      </td>
      <td>
        <p>:)</p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <table>
    <thead>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>10 10 2</p>
        </td>
        <td>
          <p>:(</p>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
  Escola de Inverno da Maratona - Erechim RS - 2015</p>
</div>