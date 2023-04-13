<p><a href="https://www.beecrowd.com.br/repository/UOJ_2739_en.html">beecrowd.com.br/repository/UOJ_2739_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2739 </span>
                            <h1>Payday</h1>
                            <div>
                              <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>The Central Bank of Financing lost many registers after a server failure that happened last October. The collection dates for the parcels where lost.</p>
                            <p>The bank requested your help to select the names and day of month in which each client must pay theirs parcel.</p>
                            <p>OBS: The day of month must be an <b>integer</b>.</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>loan</caption>
                          <tbody><tr>
                          <td><strong>Column</strong></td>
                          <td><strong>Type</strong></td>
                        </tr>
                        <tr>
                          <td>id (PK)</td>
                          <td>integer</td>
                        </tr>
                        <tr>
                          <td>name</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>value</td>
                          <td>numeric</td>
                        </tr>
                        <tr>
                          <td>payday</td>
                          <td>timestamp (ISO YMD)</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Table</h2>
                  <div>
                  <table>
                  <caption>loan</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>value</strong></td>
                  <td><strong>payday</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Cristian Ghyprievy</td>
                  <td>3000.50</td>
                  <td>2017-10-19</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>John Serial</td>
                  <td>10000</td>
                  <td>2017-10-10</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Michael Seven</td>
                  <td>5000.40</td>
                  <td>2017-10-17</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Joana Cabel</td>
                  <td>2000</td>
                  <td>2017-10-05</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Miguel Santos</td>
                  <td>4050</td>
                  <td>2017-10-20</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>day</strong></td>
        </tr>
        <tr>
          <td>Cristian Ghyprievy</td>
          <td>19</td>
        </tr>
        <tr>
          <td>John Serial</td>
          <td>10</td>
        </tr>
        <tr>
          <td>Michael Seven</td>
          <td>17</td>
        </tr>
        <tr>
          <td>Joana Cabel</td>
          <td>5</td>
        </tr>
        <tr>
          <td>Miguel Santos</td>
          <td>20</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>