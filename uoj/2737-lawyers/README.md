<p><a href="https://www.beecrowd.com.br/repository/UOJ_2737_en.html">beecrowd.com.br/repository/UOJ_2737_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2737 </span>
                            <h1>Lawyers</h1>
                            <div>
                              <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>The manager of Mangojata Lawyers requested a report on the current lawyers.</p>
                            <p>The manager wants you to show him the name of the lawyer with the most clients, the one with the fewest and the client average considering all lawyers.</p>
                            <p>OBS: Before presenting the average, show a field called <b>Average</b> to make the report more readable. The average must be presented as an integer.</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>lawyers</caption>
                          <tbody><tr>
                          <td><strong>Column</strong></td>
                          <td><strong>Type</strong></td>
                        </tr>
                        <tr>
                          <td>register (PK)</td>
                          <td>integer</td>
                        </tr>
                        <tr>
                          <td>name</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>customers_number</td>
                          <td>integer</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Tables</h2>
                  <div>
                  <table>
                  <caption>lawyers</caption>
                  <tbody><tr>
                  <td><strong>register</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>customers_number</strong></td>
                </tr>
                <tr>
                  <td>1648</td>
                  <td>Marty M. Harrison</td>
                  <td>5</td>
                </tr>
                <tr>
                  <td>2427</td>
                  <td>Jonathan J. Blevins</td>
                  <td>15</td>
                </tr>
                <tr>
                  <td>3365</td>
                  <td>Chelsey D. Sanders</td>
                  <td>20</td>
                </tr>
                <tr>
                  <td>4153</td>
                  <td>Dorothy W. Ford</td>
                  <td>16</td>
                </tr>
                <tr>
                  <td>5525</td>
                  <td>Penny J. Cormier</td>
                  <td>6</td>
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
          <td><strong>customers_number</strong></td>
        </tr>
        <tr>
          <td>Chelsey D. Sanders</td>
          <td>20</td>
        </tr>
        <tr><td>Marty M. Harrison</td>
          <td>5</td>
        </tr>
        <tr>
          <td>Average</td>
          <td>12</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>