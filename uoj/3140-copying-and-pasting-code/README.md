<p><a href="https://www.beecrowd.com.br/repository/UOJ_3140_en.html">beecrowd.com.br/repository/UOJ_3140_en.html</a></p><hr>
              <div>
                <span>URI Online | 3140</span>
                <h1>Copying and Pasting Code</h1>
                <div>
                  <p>By Roger Eliodoro Condras, UFSC-ARA <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
                </div>
                <strong>Timelimit: 1</strong>
              </div>
              <div>
              <div>
                <p>During the pandemic, with the temporary suspension of the academic calendar at UFSC, Lucas has taken advantage of his free time to take several online courses and learn to use new technologies and programming libraries.</p>
                <p>He recently participated in a free bootcamp on the use of Node.js and the ReactJS library and fell in love. He liked it so much that he decided to port a website that he had created in HTML for this new format.</p>
                <p>Luckily for Lucas, he can reuse most of the HTML scripts, but some parts are no longer necessary, since Node.js and + ReactJS start generating them automatically. As there are several files for him to analyze and give control + c, control + v in the codes, he would like your help to speed up the process.</p>
                <p>Given an HTML file, you must write a program that returns only the content between the "&lt;body&gt;" and "&lt;/body&gt;" tags, everything else must be ignored.</p>
                <p>Since Lucas is a capricious guy, the code is properly indented. In the opening and closing lines of the body tag there is nothing but the tag itself and indent spaces.</p>
              </div>
              <h2>Input</h2>
              <div>
                <p>The entry has several lines, the lines of the HTML file provided by Lucas, and ends with EOF. Each line consists of a sequence of printable characters from the ASCII Table and it is guaranteed that none of them is longer than 1,000 characters or is blank.</p>
                <p>The body opening and closing tags, "&lt;body&gt;" and "&lt;/body&gt;" respectively, are guaranteed to appear only once in the entire input file.</p>
              </div>
              <h2>Output</h2>
              <div>
                <p>You must print all the lines between the "&lt;body&gt;" and "&lt;/body&gt;" tags without including them and keeping the exact original formatting of the file.</p>
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
            </p><pre style="font-family: 'Courier New', Courier, monospace;">&lt;html&gt; &lt;head&gt; &lt;title&gt;Meu primeiro programa em HTML&lt;/title&gt; &lt;/head&gt; &lt;body&gt; &lt;h1&gt;Hello World!&lt;/h1&gt; &lt;/body&gt; &lt;/html&gt;</pre>
            <p></p>
          </td>
          <td>
          <p>
        </p><pre style="font-family: 'Courier New', Courier, monospace;">         &lt;h1&gt;Hello World!&lt;/h1&gt;</pre>
        <p></p>
      </td>
    </tr>
  </tbody>
</table>
<div></div>
  <p>
  Aquecimento - II Maratona UFSC Campus Araranguá</p>
</div>