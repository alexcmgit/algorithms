<p><a href="https://www.beecrowd.com.br/repository/UOJ_2741_en.html">beecrowd.com.br/repository/UOJ_2741_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2741 </span>
                            <h1>Students Grades</h1>
                            <div>
                              <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>The semester is over at South Transylvania University. Every grade was closed, and only Alchemy 104 haven’t published its list of approved students.</p>
                            <p>Therefore, you should show the word '<b>Approved: </b>' alongisde the the name of a student and the grade, for those who have been approved (<b>grade</b> ≥7).</p>
                            <p>Remember to sort the list by grade (higher grades first).</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>students</caption>
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
                          <td>grade</td>
                          <td>numeric</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Tables</h2>
                  <div>
                  <table>
                  <caption>students</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>grade</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Terry B. Padilla</td>
                  <td>7.3</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>William S. Ray</td>
                  <td>0.6</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Barbara A. Gongora</td>
                  <td>5.2</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Julie B. Manzer</td>
                  <td>6.7</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Teresa J. Axtell</td>
                  <td>4.6</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>Ben M. Dantzler</td>
                  <td>9.6</td>
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
          <td><strong>grade</strong></td>
        </tr>
        <tr>
          <td>Approved: Ben M. Dantzler</td>
          <td>9.6</td>
        </tr>
        <tr>
          <td>Approved: Terry B. Padilla</td>
          <td>7.3</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>