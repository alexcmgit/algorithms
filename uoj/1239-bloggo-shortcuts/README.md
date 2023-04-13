<p><a href="https://www.beecrowd.com.br/repository/UOJ_1239_en.html">beecrowd.com.br/repository/UOJ_1239_en.html</a></p><hr>
    <div>
      <span>URI Online | 1239</span>
      <h1>Bloggo Shortcuts </h1>
      <div><p>
         By TopCoder* <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/us.gif" style="width: 16px; height: 11px;"> USA</p>
      </div>
      <strong>Timelimit: 1</strong>
    </div>
    <div>
    <div>
      <p>
       You are helping to develop a weblog-management system called bloggo. Although bloggo pushes all content to the front end of a website in HTML, not all content authors enjoy using HTML tags in their text. To make their lives easier, bloggo offers a simple syntax called <i>shortcuts</i> to achieve some HTML textual effects. Your job is to take a document written with shortcuts and translate it into proper HTML.</p>
      <br>
      <p>
       One shortcut is used to make italicized text. HTML does this with the &lt;i&gt; and &lt;/i&gt; tags, but in bloggo, an author can simply enclose a piece of text using two instances of the underscore character, '_'. Thus, where a content author writes</p>
      <pre>  You _should_ see the baby elephant at the zoo!</pre>
      <p>
       bloggo will publish the following instead.</p>
      <pre>  You &lt;i&gt;should&lt;/i&gt; see the baby elephant at the zoo!</pre>
      <p>
       Another shortcut serves to render text in boldface, which HTML accomplishes with &lt;b&gt; and &lt;/b&gt; tags. Bloggo lets content authors do the same with paired instances of the asterisk character, '*'. When a content author writes the text</p>
      <pre>  Move it from *Receiving* to *Accounts Payable*.</pre>
      <p>
       it will end up on the website as</p>
      <pre>  Move it from &lt;b&gt;Receiving&lt;/b&gt; to &lt;b&gt;Accounts Payable&lt;/b&gt;.</pre>
    </div>
    <h2>Input</h2>
    <div>
      <p>
      The input contains several test cases. Each test case is composed by one line that contais a string <b>text</b>, containing zero or more usages of the italic and boldface shortcuts. Each <b>text</b> is between 1 and 50 characters long, inclusive. The only characters allowed in <b>text</b> are the alphabetic characters 'a' to 'z' and 'A' to 'Z', the underscore '_', the asterisk '*', the space character, and the punctuation symbols ',', ';', '.', '!', '?', '-', '(', and ')'. The underscore '_' occurs in <b>text</b> an even number of times. The asterisk '*' occurs in <b>text</b> an even number of times. No substring of <b>text</b> enclosed by a balanced pair of underscores or by a balanced pair of asterisks may contain any further underscores or asterisks. <br>
      <br> The end of input is determined by EOF.</p>
    </div>
    <h2>Output</h2>
    <div>
      <p>
       Translate each input <b>text</b> into HTML as demonstrated by the examples above (and below). To render a span of text in italics in HTML, you must start with the &lt;i&gt; tag and end with the &lt;/i&gt; tag. For boldface text, start with &lt;b&gt; and end with &lt;/b&gt;. Print one <b>translated text</b> per line at standard output.</p>
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
            <p>You _should_ see the new walrus at the zoo!<br>
             Move it from *Accounts Payable* to *Receiving*.<br>
             I saw _Chelydra serpentina_ in *Centennial Park*.<br>
             _ _ __ _ yabba dabba _ * dooooo * ****<br>
             _now_I_know_*my*_ABC_next_time_*sing*it_with_me</p>
          </td>
          <td>
            <p>You &lt;i&gt;should&lt;/i&gt; see the new walrus at the zoo!<br>
             Move it from &lt;b&gt;Accounts Payable&lt;/b&gt; to &lt;b&gt;Receiving&lt;/b&gt;.<br>
             I saw &lt;i&gt;Chelydra serpentina&lt;/i&gt; in &lt;b&gt;Centennial Park&lt;/b&gt;.<br>
             &lt;i&gt; &lt;/i&gt; &lt;i&gt;&lt;/i&gt; &lt;i&gt; yabba dabba &lt;/i&gt; &lt;b&gt; dooooo &lt;/b&gt; &lt;b&gt;&lt;/b&gt;&lt;b&gt;&lt;/b&gt;<br>
             &lt;i&gt;now&lt;/i&gt;I&lt;i&gt;know&lt;/i&gt;&lt;b&gt;my&lt;/b&gt;&lt;i&gt;ABC&lt;/i&gt;next&lt;i&gt;time&lt;/i&gt;&lt;b&gt;sing&lt;/b&gt;it&lt;i&gt;with&lt;/i&gt;me</p>
          </td>
        </tr>
      </tbody>
    </table>
    <p>
  </p><p>
   * This problem is of autorship and property of TopCoder (www.topcoder.com/tc) and adapted by M.C. Pinto for authorized use in URI OJ.<br>
  * Unauthorized reproduction of this problem statement without the prior written consent of TopCoder, Inc. is strictly prohibited.</p>
</div>