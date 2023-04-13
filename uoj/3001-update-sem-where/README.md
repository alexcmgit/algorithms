<p><a href="https://www.beecrowd.com.br/repository/UOJ_3001_en.html">beecrowd.com.br/repository/UOJ_3001_en.html</a></p><hr>
<div>
  <span>URI Online Judge <strong>SQL</strong> | 3001 </span>
  <h1>Update sem Where</h1>
  <div>
    <p>Gustavo Moraes <img src="https://resources.urionlinejudge.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
  </div>
  <strong>Timelimit: 1</strong>
</div>
<div>
  <div>
    <p>
    Your friend Zé Maria is in an ambush because he made an update without a where and end up zeroing all values from the price column. For your luck, the price can be recalculated knowing the product type.</p>
    <ul>
      <li>If the product type is equal to A, the price will be 20.0</li>
      <li>If the product type is equal to B, the price will be 70.0</li>
      <li>If the product type is equal to C, the price will be 530.5</li>
    </ul>
    <p>
    Your job is to show the name and price of all products. You must show the products in groups by the following order: first, all products form type A, second type B, and lastly the type C. Furthermore, the products in each group (A, B, C) must be printed in descending order by ID.</p>
  </div>
  <div>
    <h2>Schema</h2>
    <div>
      <table>
        <caption>value_table</caption>
        <tbody>
          <tr>
            <td><strong>Column</strong></td>
            <td><strong>Type</strong></td>
          </tr>
          <tr>
            <td>id</td>
            <td>numeric</td>
          </tr>
          <tr>
            <td>name</td>
            <td>varchar (50)</td>
          </tr>
          <tr>
            <td>type</td>
            <td>char</td>
          </tr>
          <tr>
            <td>price</td>
            <td>numeric</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div>
    <h2>Tables</h2>
    <div>
      <table>
        <caption>products</caption>
        <tbody>
          <tr>
            <td><strong>id</strong></td>
            <td><strong>name</strong></td>
            <td><strong>type</strong></td>
            <td><strong>price</strong></td>
          </tr>
          <tr>
            <td>1</td>
            <td>Monitor</td>
            <td>B</td>
            <td>0</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Headset</td>
            <td>A</td>
            <td>0</td>
          </tr>
          <tr>
            <td>3</td>
            <td>PC Case</td>
            <td>A</td>
            <td>0</td>
          </tr>
          <tr>
            <td>4</td>
            <td>Computer Desk</td>
            <td>C</td>
            <td>0</td>
          </tr>
          <tr>
            <td>5</td>
            <td>Gaming Chair</td>
            <td>C</td>
            <td>0</td>
          </tr>
          <tr>
            <td>6</td>
            <td>Mouse</td>
            <td>A</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div>
    <h2>Output Sample</h2>
    <div>
      <table>
        <tbody>
          <tr>
            <td><strong>name</strong></td>
            <td><strong>price</strong></td>
          </tr>
          <tr>
            <td>Mouse</td>
            <td>20.0</td>
          </tr>
          <tr>
            <td>PC Case</td>
            <td>20.0</td>
          </tr>
          <tr>
            <td>Headset</td>
            <td>20.0</td>
          </tr>
          <tr>
            <td>Monitor</td>
            <td>70.0</td>
          </tr>
          <tr>
            <td>Gaming Chair</td>
            <td>530.5</td>
          </tr>
          <tr>
            <td>Computer Desk</td>
            <td>530.5</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
<p>
</p>